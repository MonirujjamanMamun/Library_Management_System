from .forms import BookReviewForm
from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView
from .models import BooksModel, BookReview
from .forms import BooksForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from accounts.models import UserBankAccount
from django.contrib import messages
from transactions.models import Transaction
from transactions.views import send_transaction_email
from decimal import Decimal
from django.contrib.auth.models import User


# Create your views here.


@method_decorator(login_required, name='dispatch')
class AddBooksView(CreateView):
    model = BooksModel
    form_class = BooksForm
    template_name = 'add_books.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class DetailViews(DetailView):
    model = BooksModel
    pk_url_kwarg = 'id'
    template_name = 'details.html'


@login_required
def borrow_book(request, id):
    book_data = get_object_or_404(BooksModel, pk=id)
    account_data = get_object_or_404(UserBankAccount, user=request.user)

    accounts = Transaction.objects.filter(account=account_data).first()

    if accounts is not None:
        balance = account_data.balance
        amount = Decimal(str(book_data.borrowing_price))

        if balance >= amount:
            balance -= amount
            book_data.borrow = True
            book_data.save()
            messages.success(request, 'Borrow successfully.')

            account_data.balance = balance
            account_data.save()
            # send_transaction_email(
            #     account_data.user, account_data.balance, 'Borrow Books', 'borrow_email.html')

            return redirect('user_profiles')
        else:
            messages.error(request, 'Insufficient balance.')
    else:
        messages.error(request, 'Transaction not found.')

    return redirect('home')


@login_required
def return_book(request, id):
    book_data = get_object_or_404(BooksModel, pk=id)
    account_data = get_object_or_404(UserBankAccount, user=request.user)

    accounts = Transaction.objects.filter(account=account_data).first()

    if accounts is not None:
        balance = account_data.balance
        amount = Decimal(str(book_data.borrowing_price))

        if balance >= amount:
            balance += amount
            book_data.borrow = False
            book_data.save()
            messages.success(request, 'Return successfully.')

            account_data.balance = balance
            account_data.save()

            # send_transaction_email(
            #     account_data.user, account_data.balance, 'Borrow Books', 'borrow_email.html')

            return redirect('home')
        else:
            messages.error(request, 'Somethis is worng.')
    else:
        messages.error(request, 'Transaction not found.')

    return redirect('user_profiles')


@login_required
def book_review_create(request, book_id):
    template_name = 'review.html'
    book = get_object_or_404(BooksModel, pk=book_id)

    if request.method == 'POST':
        form = BookReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()

            return redirect('home', book_id=book_id)
    else:
        form = BookReviewForm()

    return render(request, template_name, {'book': book, 'form': form})
