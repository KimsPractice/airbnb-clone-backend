from django.db import models
from common.models import CommonModel


class Review(CommonModel):

    """Review from a User to a Room or Experience"""

    user = models.ForeignKey(
        "users.user",
        on_delete=models.CASCADE,
    )
    rooms = models.ForeignKey(
        "rooms.room",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
    )
    payload = models.TextField()
    rationg = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.user} / {self.rationg}⭐️"
