from rest_framework import serializers
from HOMEWORK_30.validators import check_is_published_status
from ads.models import Ad
from authentication.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class AdListSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(read_only=True)

    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Ad
        exclude = ['is_published', 'description']


class AdDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    # author = serializers.Charfield(default=serializers.CreateOnlyDefault()
    is_published = serializers.BooleanField(validators=[check_is_published_status])

    class Meta:
        model = Ad
        fields = '__all__'


class AdUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Ad
        exclude = ["author"]


class AdDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'
