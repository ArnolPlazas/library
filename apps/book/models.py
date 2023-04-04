from django.db import models

# managers
from .managers import AuthorManager, BookManager

class Author(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)

    objects = AuthorManager()

    class Meta:
        verbose_name = ("Author")
        verbose_name_plural = ("Authors")

    def __str__(self):
        return self.name + '-' + self.last_name



class Category(models.Model):
    name = models.CharField(max_length=30)   

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return str(self.id) + ' ' + self.name

    # def get_absolute_url(self):
    #     return reverse("Category_detail", kwargs={"pk": self.pk})

    
class Book(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ManyToManyField(Author)
    release_date = models.DateField('release date')
    cover = models.ImageField(upload_to=None)

    objects = BookManager()

    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("Book_detail", kwargs={"pk": self.pk})
