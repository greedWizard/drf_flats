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


class FlatNestedSerializer(FlatBaseSerializer):
    class Meta(FlatBaseSerializer.Meta):
        pass


class FlatReadSerializer(FlatNestedSerializer):
    city = CityReadSerializer()

    class Meta(FlatNestedSerializer.Meta):
        fields = FlatNestedSerializer.Meta.fields + [
            'id', 'city'
        ]