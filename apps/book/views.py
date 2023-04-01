from django.shortcuts import render
from django.views.generic import ListView

# models local
from .models import Author


class AuthorListView(ListView):
    context_object_name = 'author_list'
    template_name = "book/author_list.html"

    def get_queryset(self):
        return Author.objects.get_author_list()