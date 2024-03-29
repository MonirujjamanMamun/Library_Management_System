from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from transactions.forms import (
    DepositForm,
)
from transactions.models import Transaction


def send_transaction_email(user, amount, subject, template):
    message = render_to_string(template, {
        'user': user,
        'amount': amount,
    })
    send_email = EmailMultiAlternatives(subject, message, to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()


class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account
        })
        return kwargs


class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount
        account.save(
            update_fields=[
                'balance'
            ]
        )

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )
        send_transaction_email(
            self.request.user, amount, "Deposite Message", "deposite_email.html")
        return super().form_valid(form)
