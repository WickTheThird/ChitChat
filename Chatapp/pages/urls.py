from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginRequest, name='login'),
    path('register/', views.registerRequest, name='register'),
    path('logout/', views.logoutRequest, name='logout'),
    path("home/", views.home, name='home'),
]

