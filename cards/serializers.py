from django.contrib.auth.models import AbstractUser
from rest_framework import serializers
from cards.models import Card, User


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']
