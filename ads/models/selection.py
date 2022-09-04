from django.db import models

from ads.models import Ad
from authentication.models import User


class Selection(models.Model):
    ads = models.ManyToManyField(Ad)
    name = models.CharField(max_length=30, default='Подборка')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'

    def __str__(self):
        return self.name
