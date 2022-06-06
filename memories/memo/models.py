from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class InMemories(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(
        default=None,
        null=True,
        blank=True,
        max_length=255
    )
    comment = models.TextField()
