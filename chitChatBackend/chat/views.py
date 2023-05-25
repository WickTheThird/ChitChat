from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse

from rest_framework import viewsets

from . import forms
from . import serialisers
from . import models

def index(request):
    return render(request=request, template_name='index.html')

#> API
class LoginViewset(viewsets.ModelViewSet):
    serializer_class = serialisers.Login
    queryset = models.Users.objects.all()

class SignupViewset(viewsets.ModelViewSet):
    serializer_class = serialisers.Signup
    queryset = models.Users.objects.all()
