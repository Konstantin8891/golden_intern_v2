from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class InMemories(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        verbose_name='Заголовок',
        help_text='Введите заголовок',
        max_length=255
    )
    comment = models.TextField(
        verbose_name='Воспоминание',
        help_text='Введите воспоминание',
    )
    location = models.PointField(
        srid=4326
    )

    class Meta:
        verbose_name_plural = 'In memories'
