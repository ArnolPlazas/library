from django.db import models
from django.db.models import Avg, Sum, Count
from django.db.models.functions import Lower

class LoanManager(models.Manager):
    """
    procedures for loans
    """
    def loans_average_ages(self, book):
        result = self.filter(
            book__id = book
        ).aggregate(
            average_age= Avg('lector__age'),
            sum_age= Sum('lector__age')
        )
        return 
    
    def num_books_loan(self):
        result = self.values(
            'book' # acomular en base a libro
        ).annotate(
            num_loans = Count('book'),
            title=Lower('book__title')
        )
        for r in result:
            print('======')
            print(r, r['num_loans'])
        return result