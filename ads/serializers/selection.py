from rest_framework import serializers

from ads.models import Selection, Ad
from ads.serializers.ad import AdDetailSerializer


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ['id', 'name']


class SelectionDetailSerializer(serializers.ModelSerializer):
    ads = AdDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    ads = serializers.SlugRelatedField(
        required=False,
        slug_field='id',
        many=True,
        queryset=Ad.objects.all(),
    )

    class Meta:
        model = Selection
        fields = '__all__'

    def is_valid(self, raise_exception=True):
        self._ads = self.initial_data.pop('ads')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        selection = Selection.objects.create(**validated_data)
        for ad in self._ads:
            ad_obj = Ad.objects.get(id=ad)
            selection.ads.add(ad_obj)

        selection.save()
        return selection


class SelectionUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    ads = serializers.SlugRelatedField(
        required=False,
        slug_field='id',
        many=True,
        queryset=Ad.objects.all(),
    )
    owner = serializers.CharField(read_only=True)

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'
