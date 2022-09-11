from django.db import models

from ads.models.category import Category
from authentication.models import User
from django.core.validators import MinValueValidator, MinLengthValidator


class Ad(models.Model):
    name = models.CharField(max_length=60, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    price = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    description = models.TextField(max_length=300, default='', null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-price']

    def __str__(self):
        return self.name
