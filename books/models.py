from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=10)
    status = models.BooleanField(default=True)
