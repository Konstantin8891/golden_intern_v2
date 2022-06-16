from django.contrib.auth import get_user_model
from django.contrib.gis.db.models import PointField
from django.db import models

User = get_user_model()


class InMemories(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        verbose_name='Заголовок',
        help_text='Введите название воспоминания',
        max_length=255
    )
    comment = models.TextField(
        verbose_name='Воспоминание',
        help_text='Введите текст воспоминания'
    )
    location = PointField(srid=4326)

    class Meta:
        verbose_name_plural = 'In memories'

    def __str__(self):
        return self.title
