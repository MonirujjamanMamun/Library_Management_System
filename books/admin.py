from django.contrib import admin
from . models import BooksModel, BookReview
# Register your models here.

admin.site.register(BooksModel)
admin.site.register(BookReview)
