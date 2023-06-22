from cards.views import CardViewSet, UserViewSet
from django.conf.urls import include
from django.urls import path
from cards import views

card_list = CardViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
card_detail = CardViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = [
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>', user_list, name='user-detail'),
    path('cards/', card_list, name='card_list'),
    path('cards/<int:pk>', card_detail, name='card_detail'),
]
