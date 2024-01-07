from django.shortcuts import render
from books.models import BooksModel


def profile(request):
    books = BooksModel.objects.all()
    return render(request, 'profile_data.html', {'books': books})
