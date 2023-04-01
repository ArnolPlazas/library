from django.db import models

class AuthorManager(models.Manager):
    """
    managers for author model
    """

    def look_for_author(self, kword):
        result =self.filter(
            name__icontains = kword
            )
        return result