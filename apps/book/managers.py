import datetime

from django.db import models
from django.db.models import Q, Count


class AuthorManager(models.Manager):
    """
    managers for author model
    """

    def look_for_author(self, kword):
        result =self.filter(
            Q(name__icontains = kword) | Q(last_name__icontains = kword)
             )
        return result
    
    def look_for_author2(self, kword):
        result =self.filter(
            name__icontains = kword
             ).exclude(Q(nationality__icontains = 'Argentino') | Q(nationality__icontains = 'Mexicano'))
        return result
    
    # def look_for_author3(self):
    #     result =self.filter(
    #         age__gt=40,
    #         age__lt=60
    #          ).order_by('last_name', age)
    #     return result


class BookManager(models.Manager):
    """
    managers for book model
    """

    def list_books(self, kword):
        result =self.filter(
            title__icontains=kword,
            release_date__range=('2000-01-01', '2005-01-01')
             )
        return result
    
    def list_books2(self, kword, date_start, date_end):
        date_start = datetime.datetime.strptime(date_start, '%Y-%m-%d').date()
        date_end = datetime.datetime.strptime(date_end, '%Y-%m-%d').date()

        result =self.filter(
            title__icontains=kword,
            release_date__range=(date_start, date_end)
             )
        return result
    def list_books_by_category(self, category):
        return self.filter(
            category__id= category
        ).order_by('title')

    def add_author_book(self, book_id, author):
        book = self.get(id=book_id)
        book.author.add(author)
        return book
    
    def remove_author_book(self, book_id, author):
        book = self.get(id=book_id)
        book.author.remove(author)
        return book
    def count_num_loans(self):
        # agregate: returns a dictionary
        result = self.aggregate(
            num_loans = Count('book_loan')
        )
        return result
    
    def num_books_loan(self):
        result = self.annotate(
            num_loans = Count('book_loan')
        )
        for r in result:
            print('======')
            print(r, r.num_loans)
        return result
    


class CategoryManager(models.Manager):
    """
    managers for category model
    """
    def category_by_author(self, author):
        return self.filter(
            category_book__author__id=author
        ).distinct()

    def list_book_categories(self):
        # annotate returns a querySet
        result = self.annotate(
            num_books = Count('category_book')
        )
        for r in result:
            print('********')
            print(r, r.num_books)
        return result