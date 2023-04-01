from django.shortcuts import render
from django.views.generic import ListView

# models local
from .models import Author


class AuthorListView(ListView):
    context_object_name = 'author_list'
    template_name = "book/author_list.html"

    def get_queryset(self):
        key_word = self.request.GET.get('kword', '')
        return Author.objects.look_for_author2(key_word)