from django.shortcuts import render
# from django.views.generic import TemplateView
# Create your views here.


# class HomeViews(TemplateView):
#     template_name = 'home.html'


from books.models import BooksModel, BookReview
from categorys.models import Category


def home(request, category_slug=None):
    books = BooksModel.objects.all()
    rating = BookReview.objects.all()
    if category_slug is not None:
        categorys = Category.objects.get(slug=category_slug)
        books = BooksModel.objects.filter(category_name=categorys)
    categorys = Category.objects.all()
    return render(request, 'home.html', {"books": books, 'categorys': categorys, 'rating': rating})
