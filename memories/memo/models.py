from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class InMemories(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=255
    )
    comment = models.TextField(verbose_name='Воспоминание')
    location = models.PointField(srid=4326)

    class Meta:
        verbose_name_plural = 'In memories'

    def __str__(self):
        return self.title
