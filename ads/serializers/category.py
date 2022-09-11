from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ads.models import Category


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.CharField(
        max_length=10,
        validators=[UniqueValidator(queryset=Category.objects.all())]
    )

    class Meta:
        model = Category
        fields = '__all__'
