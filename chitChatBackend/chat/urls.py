from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'login', views.LoginViewset, basename='login')
router.register(r'signup', views.SignupViewset, basename='signup')
router.register(r'message', views.MessageViewset, basename='message')

urlpatterns = [
    path("", views.index),
    path("api/login/", views.LoginViewset.as_view({'post': 'post'}), name="login"),
    path("api/signup/", views.SignupViewset.as_view({'post': 'post'}), name="signup"),
    path("api/message/", views.MessageViewset.as_view({'sentFrom': 'sentFrom', 'get': 'get', 'delete':'delete', 'patch': 'patch'}), name="message"),
]
