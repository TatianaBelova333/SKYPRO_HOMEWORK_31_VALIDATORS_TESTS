from ads.models import Location
from authentication.models import User

from rest_framework import serializers


class UserListSerializer(serializers.ModelSerializer):
    total_ads = serializers.IntegerField(required=True)
    locations = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
        many=True,
    )

    class Meta:
        model = User
        exclude = [
            'password',
            'last_login',
            'is_superuser',
            'email',
            'is_staff',
            'is_active',
            'groups',
            'user_permissions',
            'date_joined',
        ]


class UserDetailSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
        many=True,
    )

    class Meta:
        model = User
        exclude = [
            'password',
            'last_login',
            'is_superuser',
            'email',
            'is_staff',
            'is_active',
            'groups',
            'user_permissions',
            'date_joined',
        ]


class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    locations = serializers.SlugRelatedField(
        required=False,
        slug_field='name',
        many=True,
        queryset=Location.objects.all(),
    )

    class Meta:
        model = User
        exclude = [
            'last_login',
            'is_superuser',
            'email',
            'is_staff',
            'is_active',
            'groups',
            'user_permissions',
            'date_joined',
        ]

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop('locations')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for location in self._locations:
            location_obj, _ = Location.objects.get_or_create(name=location)
            user.locations.add(location_obj)

        user.set_password(validated_data["password"])

        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        required=False,
        slug_field='name',
        many=True,
        queryset=Location.objects.all(),
    )

    class Meta:
        model = User
        exclude = [
            'last_login',
            'is_superuser',
            'email',
            'is_staff',
            'is_active',
            'groups',
            'user_permissions',
            'date_joined',
        ]

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop('locations')
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        if self._locations:
            user.locations.clear()
            for location in self._locations:
                location_obj, _ = Location.objects.get_or_create(name=location)
                user.locations.add(location_obj)

        user.save()
        return user


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']