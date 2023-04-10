from django.db import models
from django.db.models import Avg, Sum

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
        return result
