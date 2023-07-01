
#? DJANGO
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout # <-- just add these here in case i need them
# from django.contrib import messages
# from django.http import JsonResponse

#? REST
from rest_framework import viewsets, status
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

#? FILES
from . import serialisers
from . import models

#? ENCRYPTION
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#> Session gen
class Session:

    #! NOTE THAT DATA MIGHT BE IN JSON SO KEEP IN MIND IN CASE ISSUES ARRISE

    def __init__(self):

        self.key = get_random_bytes(128)
        self.cipher = AES.new(self.key, AES.MODE_EAX)

    def encrypt(self, data):

        ciphertext, tag = self.cipher.encrypt_and_digest(data)
        return ciphertext, tag

    def decrypt(self, ciphertext, tag):

        plaintext = self.cipher.decrypt_and_verify(ciphertext, tag)
        return plaintext


#> API
class LoginViewset(GenericViewSet):
    serializer_class = serialisers.Login


    def login(self, request) -> (Response or None):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            username=serializer.validated_data['name'][0]
            email=serializer.validated_data['email'][0]

            print("\nUsername:", username, "\nEmail:", email, '\n')

            user = models.User.objects.filter(username=username, email=email).first()
            state = authenticate(request, username=username, password=user.password1)
            
            if not state:
                return Response({"message": "Incorrect password or username"}, status=status.HTTP_400_BAD_REQUEST)

            login(request, user)

            return Response({"message": "User logged in successfully"}, status=status.HTTP_200_OK)

        else:
            return Response(serializer.validated_data, status=status.HTTP_400_BAD_REQUEST)


class SignupViewset(viewsets.ModelViewSet):
    serializer_class = serialisers.Signup
    queryset = models.Users.objects.all()


    def post(self, request) -> (Response or None):
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

# An alternative
# class UserLoginView(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serialisers = self.serializer_class(data=request.data, context={'request': request})

#         serialisers.is_valid(raise_exception=True)
#         user = serialisers.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)

#         return Response({'token': token.key})

#? Messsging
class MessageViewset(viewsets.ModelViewSet):
    serializer_class = serialisers.Messages


    def get(self, request) -> (Response or None):
        messages = models.Messages.objects.all()
        serializer = serialisers.Messages(data=request.data, many=True)

        if serializer.is_valid() and request.method == 'GET':
            return Response(messages, status=status.HTTP_200_OK)

        return Response({"message": "Failed to get messages"}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request) -> (Response or None):
        serializer = serialisers.Messages(data=request.data)

        if serializer.is_valid() and request.method == 'DELETE':
            message = serializer.validated_data['message'][0]
            print(message)
            models.Messages.objects.filter(message=message).delete()

            return Response({"message": "Message deleted successfully"}, status=status.HTTP_200_OK)

        return Response({"message": "Failed to delete message"}, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request) -> (Response or None):
        serialiser = serialisers.Messages(data=request.data)

        if serialiser.is_valid() and request.method == 'PATCH':
            message = serialiser.validated_data['message'][0]
            print(message)
            models.Messages.objects.filter(message=message).update(message=message)

            return Response({"message": "Message updated successfully"}, status=status.HTTP_200_OK)

        return Response({"message": "Failed to update message"}, status=status.HTTP_400_BAD_REQUEST)


    def sentTo(self, request) -> (Response or None):
        serialiser = serialisers.Messages(data=request.data)

        if serialiser.is_valid() and request.method == 'POST':
            message = serialiser.validated_data['message'][0]
            print(message)
            models.Messages.objects.create(message=message)

            return Response({"message": "Message sent successfully"}, status=status.HTTP_200_OK)


    def sentFrom(self, request) -> (Response or None):
        serialiser = serialisers.Messages(data=request.data)

        if serialiser.is_valid() and request.method == 'POST':
            message = serialiser.validated_data['message'][0]
            print(message)
            models.Messages.objects.create(message=message)

            return Response({"message": "Message sent successfully"}, status=status.HTTP_200_OK)






