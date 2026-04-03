from django.urls import path

from . import views

urlpatterns = [
    path('/profile', views.OwnProfileView.as_view(), name='own_profile'),
    path('/users/<str:username>', views.UserProfileView.as_view(), name='user_profile'),
    path('/users/<str:username>/follow', views.FollowView.as_view(), name='follow'),
]
