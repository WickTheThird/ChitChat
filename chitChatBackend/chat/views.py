from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.http import JsonResponse

from rest_framework import viewsets, status
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# from rest_framework.decorators import action
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
            username=serializer.validated_data['name'][0]
            email=serializer.validated_data['email'][0]

            print("\nUsername:", username, "\nEmail:", email, '\n')

            user = models.User.objects.filter(username=username, email=email).first()
            login(request, user)

            return Response({"message": "User logged in successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.validated_data, status=status.HTTP_400_BAD_REQUEST)


class SignupViewset(viewsets.ModelViewSet):
    serializer_class = serialisers.Signup
    queryset = models.Users.objects.all()

    def post(self, request, *args, **kwargs) -> (Response or None):
        serialiser = self.get_serializer(data=request.data)

        if serialiser.is_valid():
            message = serialiser.perform_create(serialiser)
            if message is True:
                return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
            return Response({"message:" "Failed to create new user."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serialiser.validated_data, status=status.HTTP_400_BAD_REQUEST)

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
