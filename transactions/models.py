from django.db import models
from accounts.models import UserBankAccount
# Create your models here.


class Transaction(models.Model):
    account = models.ForeignKey(
        UserBankAccount, related_name='transactions', on_delete=models.CASCADE, default=1)

    amount = models.DecimalField(decimal_places=2, max_digits=12)
    # timestamp = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ['timestamp']
