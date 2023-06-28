from cards.views import AllCardViewSet, OneCardViewSet, ProfileViewSet, UserSentViewSet, UserReceivedViewSet, ThisUserFollowsListViewSet, FollowsThisUserViewSet, FollowUserViewSet, UnfollowUserViewSet
from django.conf.urls import include
from django.urls import path
from cards import views


urlpatterns = [

    path('api/profile/<username>/',
         views.ProfileViewSet.as_view(), name='user_detail'),

    path('api/cards/', views.AllCardViewSet.as_view(), name='card_list'),

    path('api/cards/<int:pk>/', views.OneCardViewSet.as_view(), name='card_detail'),

    path('api/cards/sent/', views.UserSentViewSet.as_view(), name='user_sent'),

    path('api/cards/received/',
         views.UserReceivedViewSet.as_view(), name='user_received'),

    path('api/user_following/', views.ThisUserFollowsListViewSet.as_view(),
         name='user_following'),

    path('api/user_followers/',
         views.FollowsThisUserViewSet.as_view(), name="user_followers"),

    path('api/follow_user/',
         views.FollowUserViewSet.as_view(), name="follow_user"),

    path('api/unfollow_user/<int:pk>',
         views.UnfollowUserViewSet.as_view(), name="unfollow_user")



]
