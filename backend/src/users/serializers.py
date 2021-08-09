from .models import Profile
from flats.serializers import FlatReadSerializer
from django.db.models.base import Model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class UserBaseSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', ]


class ProfileBaseSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'surname', 'phone']


class ProfileReadSerializer(ProfileBaseSerializer):
    class Meta(ProfileBaseSerializer.Meta):
        fields = ProfileBaseSerializer.Meta.fields + [
            'id',
        ]


class UserReadSerializer(UserBaseSerializer):
    profile = ProfileReadSerializer(many=False)

    class Meta(UserBaseSerializer.Meta):
        fields = UserBaseSerializer.Meta.fields + [
            'id', 'profile', 'username',
        ]


class UserPostSerializer(UserBaseSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    surname = serializers.CharField()
    phone = serializers.CharField()
    password = serializers.CharField()
    repeat_password = serializers.CharField()
    email = serializers.CharField()

    class Meta(UserBaseSerializer.Meta):
        fields = UserBaseSerializer.Meta.fields + [
            'first_name', 'last_name', 'surname',
            'phone', 'password', 'repeat_password',
        ]