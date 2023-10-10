from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'login', views.LoginViewset, basename='login')
router.register(r'signup', views.SignupViewset, basename='signup')

urlpatterns = [
    path("read/", views.LoginViewset.as_view(), name="login"),
    path("api/signup/", views.SignupViewset.as_view({'post': 'post'}), name="signup"),
    path("check-session/", views.check_session, name='active_session'),
]
