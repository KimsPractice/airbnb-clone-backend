from django.db import models

class Houst(models.Model):

    """
    Model Definition for houses
    """
    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)