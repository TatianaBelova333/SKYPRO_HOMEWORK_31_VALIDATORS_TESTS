from django.db import models
from django.core.validators import MinLengthValidator


class Category(models.Model):
    name = models.CharField(max_length=50, default='')
    slug = models.SlugField(max_length=10, null=True, unique=True, validators=[MinLengthValidator(5)])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name
