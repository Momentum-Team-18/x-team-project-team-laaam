from django.shortcuts import render
from rest_framework import viewsets
from models import User, Card
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from serializers import UserSerializer, CardSerializer

# Create your views here.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]
    