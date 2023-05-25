from rest_framework import serializers
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from . import models
import re

class Login(serializers.ModelSerializer):
    class Meta:
        model = models.Users
        fields = ('name', 'password1')

    def validate(self, data):
        user = authenticate(name=data['name'], password1=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        return data

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
