from regions.serializers import CityReadSerializer
from flats.models import Adress
from rest_framework import serializers


class FlatBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adress
        fields = [
            'flat_number', 'street', 'house', 'struct'
        ]


class FlatPostSerializer(FlatBaseSerializer):
    city_id = serializers.IntegerField()

    class Meta(FlatBaseSerializer.Meta):
        fields = FlatBaseSerializer.Meta.fields + [
            'city_id'
        ]


class FlatNestedSerizlier(FlatBaseSerializer):
    class Meta(FlatBaseSerializer.Meta):
        pass


class FlatReadSerializer(FlatNestedSerizlier):
    city = CityReadSerializer()

    class Meta(FlatNestedSerizlier.Meta):
        fields = FlatNestedSerizlier.Meta.fields + [
            'id', 'city'
        ]