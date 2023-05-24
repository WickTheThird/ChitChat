from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'login', views.loginViewset, basename='login')
router.register(r'signup', views.signupViewset, basename='signup')
router.register(r'logout', views.logoutViewset, basename='logout')

urlpatterns = [
    path("", views.index),
    path("api/", include(router.urls)),
]
