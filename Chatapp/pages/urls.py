from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginRequest, name='login'),
    path('register/', views.registerRequest, name='register'),
    path('logout/', views.logoutRequest, name='logout'),
    path("home/", views.home, name='home'),
    path("user/<str:userName>", views.user,  name='user'),
    path("friend_request/<str:userName>", views.sendFriendRequest, name='friend_request'),
    path("friend_request/<str:userName>/accept", views.acceptFriendRequest, name='accept_friend_request'),
    path("friend_request/<str:userName>/decline", views.declineFriendRequest, name='decline_friend_request'),
]
