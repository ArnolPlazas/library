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