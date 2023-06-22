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

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = [
    path('api/users/<int:pk>', user_detail, name='user-detail'),
    path('api/cards/', card_list, name='card_list'),
    path('api/cards/<int:pk>', card_detail, name='card_detail'),
]
