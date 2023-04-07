from django.urls import path

from . import views

urlpatterns = [
    path(
        'authors/', 
        views.AuthorListView.as_view(), 
        name='authors'
    ),
    path(
        'books/', 
        views.BookListView.as_view(), 
        name='books'
    ),
    path(
        'books-by-category/', 
        views.BookListByCategoryView.as_view(), 
        name='books_by_category'
    ),
    path(
        'books/<pk>', 
        views.BookDetailView.as_view(), 
        name='book_detail'
    ),
]