from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator, RegexValidator

from HOMEWORK_30.validators import check_min_age
from ads.models.location import Location


class User(AbstractUser):
    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ROLES = [(MEMBER, "Пользователь"), (MODERATOR, "Модератор"), (ADMIN, "Администратор")]

    role = models.CharField(max_length=9, choices=ROLES, default=MEMBER)
    age = models.PositiveSmallIntegerField(null=True)
    locations = models.ManyToManyField(Location)
    email = models.CharField(
        max_length=254,
        null=True,
        unique=True,
        validators=[EmailValidator(),
                    RegexValidator(regex=r"(?:rambler\.ru)", inverse_match=True, message='Rambler domain not allowed')]
    )
    birthday = models.DateField(null=True, validators=[check_min_age])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return self.username
