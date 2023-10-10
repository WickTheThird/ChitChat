
#? DJANGO
# from django.shortcuts import render
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout # <-- just add these here in case i need them

#? REST
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.middleware.csrf import get_token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

#? FILES
from . import serialisers
from . import models

#> API
class LoginViewset(APIView):
    serializer_class = serialisers.Login

    def get(self, request) -> Response:
        response = Response({"message": "Set CSRF cookie"})
        response["X-CSRFToken"] = get_token(request)

        return response


    def post(self, request) -> Response:

        username = request.data['username']
        password = request.data['password']
        
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            response = Response({"message": "User logged in successfully"})
            response.set_cookie('access_token', access_token, httponly=True, samesite='None', secure=True)

            return response

        return Response({'message': 'Invalid username or password.'}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
def check_session(request):
    
    access_token = request.COOKIES.get('access_token')
    if not access_token:
        return Response({'message': 'Access token was not passed correctly'}, status=status.HTTP_403_FORBIDDEN)

    request.META['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'
    jwt_auth = JWTAuthentication()
    try:
        user, _ = jwt_auth.authenticate(request)
        if not user:
            raise Exception()
    except:
        return Response({'message': 'The token does not match with the user'}, status=status.HTTP_403_FORBIDDEN)
    
    return Response({'message': 'The user is logged in.'}, status=status.HTTP_200_OK)



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
