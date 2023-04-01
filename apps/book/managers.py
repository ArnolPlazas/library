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