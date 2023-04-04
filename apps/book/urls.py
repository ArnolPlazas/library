from django.urls import path

from . import views

urlpatterns = [
    path(
        'authors/', 
        views.AuthorListView.as_view(), 
        name='book/author_list.html'
    ),
    path(
        'books/', 
        views.BookListView.as_view(), 
        name='book/book_list.html'
    ),
]