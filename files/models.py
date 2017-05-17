from django.db import models

from books.models import Book

class ImageFile(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField()
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='images',
        blank=True
    )
