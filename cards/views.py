from django.shortcuts import render
from rest_framework import viewsets, mixins, generics, permissions
from .models import User, Card, Follow
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfileSerializer, CardSerializer, FollowSerializer

# Create your views here.


class ProfileViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class AllCardViewSet(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def post(self, request, pk, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class OneCardViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, pk, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserSentViewSet(generics.ListAPIView):
    queryset = Card.objects.all()

    def get_queryset(self):
        return self.request.user.cards_sent
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserReceivedViewSet(generics.ListAPIView):
    queryset = Card.objects.all()

    def get_queryset(self):
        return self.request.user.cards_received
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserFollowersViewSet(generics.ListAPIView):
    queryset = Follow.objects.all()

    # def get_queryset(self):
    #     return self.request.user.follows_as_follower
    serializer_class = FollowSerializer
    # permission_classes = [permissions.IsAuthenticated]


# class FollowerPostViewSet(generics.ListAPIView):
#     queryset = Card.objects.all()

#     def get_queryset(self):
#         return self.request.user.sent_by_user
#     serializer_class = CardSerializer
#     permission_classes = [permissions.IsAuthenticated]
