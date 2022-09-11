from calendar import leapdays
from datetime import date
from django.core.exceptions import ValidationError
from rest_framework import serializers


def check_min_age(birthday: date, min_age: int = 9):
    today = date.today()
    min_days_diff = 365 * min_age + leapdays(birthday.year, today.year)
    actual_days_diff = (today - birthday).days
    if actual_days_diff < min_days_diff:
        raise ValidationError(f"User's minimum age must be at least {min_age} years old")


def check_is_published_status(status: bool):
    if status is True:
        raise serializers.ValidationError('Incorrect status')
