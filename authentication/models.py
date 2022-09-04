from django.db import models
from django.contrib.auth.models import AbstractUser

from ads.models.location import Location


class User(AbstractUser):
    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ROLES = [(MEMBER, "Пользователь"), (MODERATOR, "Модератор"), (ADMIN, "Администратор")]

    role = models.CharField(max_length=9, choices=ROLES, default=MEMBER)
    age = models.PositiveSmallIntegerField(null=True)
    locations = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return self.username


"""
class User(models.Model):
    ROLES = [
        ("member", "Пользователь"),
        ("moderator", "Модератор"),
        ("admin", "Администратор")
    ]
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=30, default='', unique=True)
    password = models.CharField(max_length=50, default='')
    role = models.CharField(max_length=9, choices=ROLES, default='member')
    age = models.PositiveSmallIntegerField(null=True)
    locations = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return self.username

"""