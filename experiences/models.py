from django.db import models
from common.models import CommonModel


class Experience(CommonModel):

    """Experiences Model Definition"""

    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    name = models.CharField(max_length=250)
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()
    perk = models.ManyToManyField("experiences.Perk")

    category = models.ForeignKey(
        "categories.Category",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self) -> str:
        return self.name


class Perk(CommonModel):

    """What is included on an Experiencs"""

    name = models.CharField(max_length=100)
    details = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )
    explanation = models.TextField(
        blank=True,
        default=True,
    )

    def __str__(self) -> str:
        return self.name
