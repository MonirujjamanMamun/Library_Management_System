from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.AddBooksView.as_view(), name='add_books'),
    path('borrow/<int:id>/', views.borrow_book, name='borrow'),
    path('return/<int:id>/', views.return_book, name='return'),
    path('review/<int:book_id>/', views.book_review_create, name='review'),
    # path('review/<int:book_id>/',views.BookReviewCreateView.as_view(), name='review'),

]
