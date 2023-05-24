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

#> Entry Form
def loginRequest(request, username, useremail): #todo -> it would be better if the information would be stored in the request itself via json

   pass
                
@login_required
def logoutRequest(request, username): #todo -> it would be better if the information would be stored in the request itself via json
    pass

def signupRequest(request, username, useremail): #todo -> we need to add a new user to the Users model, once signed up
                     #todo -> proper validation needs to be added, for the form 
                     #     -> since the form is on the frontend side and the signup us a request
                     #     -> we need just to validate data and return a response on wether data
                     #     -> has been added to the database or not, thus proper validators need to be created             
    pass


#> API
class loginViewset(viewsets.ModelViewSet):
    serializer_class = serialisers.Users
    queryset = models.Users.objects.all()

class signupViewset(viewsets.ModelViewSet):
    serializer_class = serialisers.Users
    queryset = models.Users.objects.all()

class logoutViewset(viewsets.ModelViewSet):
    serializer_class = serialisers.Users
    queryset = models.Users.objects.all()
