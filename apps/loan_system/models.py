from django.db import models

# from local apps
from apps.book.models import Book

# from managers
from .managers import LoanManager


class Lector(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    age = models.PositiveIntegerField(default=0)
    

    class Meta:
        verbose_name = ("Lector")
        verbose_name_plural = ("Lectors")

    def __str__(self):
        return self.name + '-' + self.last_name

    # def get_absolute_url(self):
    #     return reverse("Lector_detail", kwargs={"pk": self.pk})
 

class Loan(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_loan')
    load_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    objects = LoanManager()
    
    class Meta:
        verbose_name = ("Loan")
        verbose_name_plural = ("Loans")

    def __str__(self):
        return self.book.title

    # def get_absolute_url(self):
    #     return reverse("Loan_detail", kwargs={"pk": self.pk})
