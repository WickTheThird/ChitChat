from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),
    path("login/str:username/str:useremail", views.login),
    path("signup/str:username/str:useremail", views.signup),
    path("logout/str:username", views.logout),
]

