from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import State, City


class CityBaseSerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ['name']


class CityPostSerializer(CityBaseSerializer):
    state_id = serializers.IntegerField()

    class Meta(CityBaseSerializer.Meta):
        fields = CityBaseSerializer.Meta.fields


class CityNestedSerializer(CityBaseSerializer):
    class Meta(CityBaseSerializer.Meta):
        fields = CityBaseSerializer.Meta.fields + [
            'id'
        ]


class StateBaseSerializer(ModelSerializer):
    class Meta:
        model = State
        fields = ['name']


class StatePostSerializer(StateBaseSerializer):
    class Meta(StateBaseSerializer.Meta):
        pass


class StateNestedSerializer(StatePostSerializer):
    class Meta(StatePostSerializer.Meta):
        fields = StatePostSerializer.Meta.fields + [
            'id'
        ]


class CityReadSerializer(CityNestedSerializer):
    state = StateNestedSerializer()

    class Meta(CityNestedSerializer.Meta):
        fields = CityNestedSerializer.Meta.fields + [
            'state'
        ]


class StateReadSerializer(StateNestedSerializer):
    cities = CityNestedSerializer(many=True)

    class Meta(StateNestedSerializer.Meta):
        fields = StateNestedSerializer.Meta.fields + [
            'cities'
        ]
