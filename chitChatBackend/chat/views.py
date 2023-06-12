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
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet


from . import serialisers
from . import models

def index(request) -> (render):
    return render(request=request, template_name='index.html')

#> API
class LoginViewset(GenericViewSet):
    serializer_class = serialisers.Login

    def post(self, request, *args, **kwargs) -> (Response or None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            
            print("\nValidated data:\n", serializer.validated_data)
            
            username = serializer.validated_data[0]#['username']
            password = serializer.validated_data[1]#['password1']
            email = serializer.validated_data[2]#['email']

            user = authenticate(request, username=username, password=password, email=email)

            if user is not None:
                login(request, user)
                return Response({"message": "User logged in successfully"}, status=status.HTTP_200_OK)
            else:
                print(serializer.validated_data)
                return Response(serializer.validated_data, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.validated_data, status=status.HTTP_400_BAD_REQUEST)


class SignupViewset(viewsets.ModelViewSet):
    serializer_class = serialisers.Signup
    queryset = models.Users.objects.all()

    def post(self, request, *args, **kwargs) -> (Response or None):
        serialiser = self.get_serializer(data=request.data)
        
        if serialiser.is_valid():
            
            print("\nValidated Data:\n", serialiser.validated_data)
            
            username = serialiser.validated_data[0]#['username']
            email = serialiser.validated_data[1]#['email']
            password1 = serialiser.validated_data[2]#['password1']
            password2 = serialiser.validated_data[3]#['password2']
            
        #? a checker on both the views and the serialiser must be put in place to check the existence of a user or not
        
        user = authenticate(request, username=username, password1=password1, password2=password2, email=email)

        print("\nThis is user\n", user)
        

    #> This overrites the method, but someting similar will have to happen when sending messages
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
