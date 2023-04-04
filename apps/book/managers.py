import datetime

from django.db import models
from django.db.models import Q


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