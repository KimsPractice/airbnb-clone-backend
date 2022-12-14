from django.db import models

class House(models.Model):

    """
    Model Definition for houses
    """
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        verbose_name="Pets Allowed ?",
        default=True, help_text="Pets Allowed")

    def __str__(self):
        return self.name