from rest_framework import serializers
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from . import models
import re

class Login(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)

    class Meta:
        model = models.Users
        fields = ('name', 'password1', 'email')

    def validate(self, data) -> (list or None):
        errors = []
        
        username = data.get('name')
        password = data.get('password1')
        email = data.get('email')
        
        #> we must validate the existance of the data provided and its correctness
        if not models.Users.objects.filter(name=username).exists():
            errors.append("Username does not exist.")
        
        if not models.Users.objects.filter(email=email).exists():
            errors.append("Email does not exist.")
        
        if not models.Users.objects.filter(password=password).exists():
            errors.append("Incorrect password.")
            
        if not models.Users.objects.filter(name=username, email=email).exists():
            errors.append("Username and email do not match.")

        return errors

    def perform_create(self, serializer):
        print("Validated data:", serializer.validated_data)
        if serializer.validated_data == []:
            return
        super().perform_create(serializer)

class Signup(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = models.Users
        fields = ('name', 'email', 'password1', 'password2')

    def validate(self, data) -> (list or None):
        errors = []
        
        username = data.get('name')
        email = data.get('email')
        password1 = data.get('password1')
        password2 = data.get('password2')
        
        #? the user technically does not exist currently but we must check that the information provided does meet certain criteria
        if models.Users.objects.filter(name=username).exists():
            errors.append("Username already exists.")

        if models.Users.objects.filter(email=email).exists():
            errors.append("Email already exists.")
        
        if not re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", email):
            errors.append("Invalid email address")

        if password1 != password2:
            errors.append("Password1 and Password2 do not match.")

        if len(password1) < 8:
            errors.append("Password must be at least 8 characters long.")

        return errors

    def create(self, validated_data) -> (object or None):
        user = models.Users.objects.create_user(
            name=validated_data['username'],
            email=validated_data['email'],
            password1=validated_data['password1'],
            password2=validated_data['password2'],
        )
        return user
    
    def perform_create(self, serializer) -> (None):
        print("Validated data: ", serializer.validated_data)
        if serializer.validated_data == []:
            return
        super().perform_create(serializer)
