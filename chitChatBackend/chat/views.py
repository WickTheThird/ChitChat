from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse

from rest_framework import viewsets, status
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
from rest_framework.response import Response

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

    #> This overrites the method, but someting similar will have to happen when sending messages;
    # def create(self, request, *args, **kwargs):
    #     # Add the message string to the validated data
    #     validated_data = dict(request.data)
    #     validated_data['message'] = 'Hello, world!'

    #     serializer = self.get_serializer(data=validated_data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

#? An alternative
# class UserLoginView(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serialisers = self.serializer_class(data=request.data, context={'request': request})
        
#         serialisers.is_valid(raise_exception=True)
#         user = serialisers.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
        
#         return Response({'token': token.key})
