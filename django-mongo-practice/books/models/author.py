from djongo import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    class Meta:
        db_table = "books_author"
        verbose_name = "author"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
