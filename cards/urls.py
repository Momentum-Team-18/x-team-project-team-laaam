from cards.views import FollowsThisUserViewSet, ThisUserFollowsViewSet, CardViewSet, ProfileViewSet, UserSentViewSet, UserReceivedViewSet
from django.conf.urls import include
from django.urls import path
from cards import views


urlpatterns = [
    path('api/profile/<int:pk>', views.ProfileViewSet.as_view(), name='user_detail'),
    path('api/cards/', views.CardViewSet.as_view(), name='card_list'),
    path('api/cards/<int:pk>', views.CardViewSet.as_view(), name='card_detail'),
    path('api/cards/sent/', views.UserSentViewSet.as_view(), name='user_sent'),
    path('api/cards/received/',
         views.UserReceivedViewSet.as_view(), name='user_received'),
    path('api/user/<int:pk>/following/',
         views.ThisUserFollowsViewSet.as_view(), name='following'),
    path('api/user/<int:pk>/followers/',
         views.FollowsThisUserViewSet.as_view(), name="follower"),

]
