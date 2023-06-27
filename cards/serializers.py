from django.contrib.auth.models import AbstractUser
from rest_framework import serializers
from cards.models import Card, User, Follow


class CardSerializer(serializers.ModelSerializer):
    '''
    Card list and card instance
    Renders username instead of pk/id
    '''
    sent_by_user = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())
    sent_to_user = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Card
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    '''
    Profile instance
    '''
    class Meta:
        model = User
        exclude = ['password']


class FollowUserSerializer(serializers.ModelSerializer):
    '''
    POST method for follow instance
    Renders username instead of pk/id
    '''
    user_this_user_is_following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ['user_this_user_is_following']


class ThisUserFollowsSerializer(serializers.ModelSerializer):
    '''
    Lists users logged-in user follows
    Renders username instead of pk/id
    '''
    user_this_user_is_following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ['user_this_user_is_following']


class FollowsThisUserSerializer(serializers.ModelSerializer):
    '''
    Lists users that follow logged-in user
    Renders username instead of pk/id
    '''
    this_user = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ['this_user']
