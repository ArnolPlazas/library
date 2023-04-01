from django.db import models

class AuthorManager(models.Manager):
    """
    managers for author model
    """

    def get_author_list(self):
        return self.all()