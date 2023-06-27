from django.contrib.auth.models import AbstractUser
from rest_framework import serializers
from cards.models import Card, User, Follow


class CardSerializer(serializers.ModelSerializer):

    sent_by_user = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())
    sent_to_user = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Card
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

class FollowUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['this_user', 'user_this_user_is_following']

class ThisUserFollowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['user_this_user_is_following']


class FollowsThisUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['this_user']
