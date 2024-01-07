from django.db import models
from django.contrib.auth.models import User
from categorys.models import Category
from accounts.models import UserBankAccount
from django.core.validators import MaxValueValidator
# Create your models here.


class BooksModel(models.Model):
    books_img = models.ImageField(
        upload_to='books/media/uploads/', blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    borrowing_price = models.FloatField()
    category_name = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=1)
    # borrower = models.OneToOneField(
    #     User, related_name='purchased', blank=True)
    borrow = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class BookReview(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BooksModel, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[
                                 MaxValueValidator(5)])

    def __str__(self):
        return f"{self.user.username}'s rating for {self.book.title}: {self.rating} stars"
