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