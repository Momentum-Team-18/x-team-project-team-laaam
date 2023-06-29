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
    Profile instance with nested CardSerializer for list of the cards 
    the user has sent and received
    '''
    cards_sent = CardSerializer(many=True, read_only=True)
    cards_received = CardSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'bio', 'date_joined', 'cards_sent', 'cards_received']


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


class UnfollowUserSerializer(serializers.ModelSerializer):
    user_this_user_is_following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ['user_this_user_is_following']


class ThisUserFollowsListSerializer(serializers.ModelSerializer):
    '''
    Lists users logged-in user follows
    Renders username instead of pk/id
    '''
    user_this_user_is_following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ['user_this_user_is_following', 'id']


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

