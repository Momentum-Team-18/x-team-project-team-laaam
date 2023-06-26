from cards.views import AllCardViewSet, AllCardViewSet, ProfileViewSet, UserSentViewSet, UserReceivedViewSet, UserFollowersViewSet
from django.conf.urls import include
from django.urls import path
from cards import views


urlpatterns = [
    path('api/profile/<int:pk>/', views.ProfileViewSet.as_view(), name='user_detail'),
    path('api/cards/', views.AllCardViewSet.as_view(), name='card_list'),
    path('api/cards/<int:pk>/', views.OneCardViewSet.as_view(), name='card_detail'),
    path('api/cards/sent/', views.UserSentViewSet.as_view(), name='user_sent'),
    path('api/cards/received/',
         views.UserReceivedViewSet.as_view(), name='user_received'),
    path('api/followers/', views.UserFollowersViewSet.as_view(),
         name='user_followers'),
]
