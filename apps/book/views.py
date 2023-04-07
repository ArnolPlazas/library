from django.shortcuts import render
from django.views.generic import ListView, DetailView

# models local
from .models import Author, Book


class AuthorListView(ListView):
    context_object_name = 'author_list'
    template_name = "book/author_list.html"

    def get_queryset(self):
        key_word = self.request.GET.get('kword', '')
        return Author.objects.look_for_author2(key_word)
    

class BookListView(ListView):
    context_object_name = 'book_list'
    template_name = "book/book_list.html"

    def get_queryset(self):
        key_word = self.request.GET.get('kword', '')
        date_start = self.request.GET.get('date_start', '')
        date_end = self.request.GET.get('date_end', '')

        if date_start and date_end:
            return Book.objects.list_books2(key_word, date_start, date_end)
        else:
            return Book.objects.list_books(key_word)

class BookListByCategoryView(ListView):
    context_object_name = 'book_list'
    template_name = "book/book_list_by_category.html"

    def get_queryset(self):
        return Book.objects.list_books_by_category('1')


class BookDetailView(DetailView):
    model = Book
    template_name = "book/detail_book.html"
