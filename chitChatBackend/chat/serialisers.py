from rest_framework import serializers
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from . import models
import re

class Login(serializers.ModelSerializer):
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)

    class Meta:
        model = models.Users
        fields = ('name', 'password1', 'email')

    def validate(self, data):
        errors = []
        
        username = data.get('name')
        password = data.get('password1')
        email = data.get('email')
        
        if not models.Users.objects.filter(name=username).exists():
            errors.append("Username does not exist.")
        
        if not models.Users.objects.filter(email=email).exists():
            errors.append("Email does not exist.")
            
        if not models.Users.objects.filter(name=username, email=email).exists():
            errors.append("Username and email do not match.")

        return errors

    def perform_create(self, serializer):
        print("Validated data:", serializer.validated_data)
        if serializer.validated_data == []:
            return
        super().perform_create(serializer)

class Signup(serializers.ModelSerializer):
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = models.Users
        fields = ('name', 'email', 'password1', 'password2')

    def validate_email(self, value):
        if models.Users.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email address already in use.")
        return value

    def validate_username(self, value):
        if models.Users.objects.filter(name=value).exists():
            raise serializers.ValidationError("Username already in use.")
        return value

    def validate_password2(self, value):
        if value != self.initial_data.get('password1'):
            raise serializers.ValidationError("Passwords do not match.")
        if len(value) < 8:
            raise serializers.ValidationError("Password is too short.")
        return value

    def create(self, validated_data):
        user = models.Users.objects.create_user(
            name=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password1'],
        )
        return user
    
    def perform_create(self, serializer):
        if serializer.validated_data == []:
            return
        super().perform_create(serializer)
