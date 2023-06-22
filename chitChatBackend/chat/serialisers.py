from rest_framework import serializers
# from django.contrib.auth import authenticate
# from django.core.exceptions import ValidationError
from . import models
import re


class Login(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)

    class Meta:
        model = models.Users
        fields = ('name', 'password1', 'email')

    def validate(self, data) -> (dict or None):
        validated_data = {}

        username = data.get('name')
        password = data.get('password1')
        email = data.get('email')

        validated_data['name'] = []
        validated_data['name'].append(username)

        validated_data['email'] = []
        validated_data['email'].append(email)

        validated_data['password1'] = []
        validated_data['password1'].append(password)

        if not models.Users.objects.filter(name=username).exists():
            validated_data['name'].append("Username does not exist.")
            raise serializers.ValidationError("Username does not exist.")


        if not models.Users.objects.filter(email=email).exists():
            validated_data['email'].append("Email does not exist.")
            raise serializers.ValidationError("Email does not exist.")

        if not models.Users.objects.filter(name=username, password1=password).exists():
            validated_data['password1'].append("Incorrect Password.")
            raise serializers.ValidationError("Incorrect Password.")

        if not models.Users.objects.filter(name=username, email=email).exists():
            validated_data['name'].append("Incorrect email address.")
            raise serializers.ValidationError("Incorrect email address.")

        return validated_data

    #! I hardly believe this will ever be called given that this is a login serializer (i will keep it here for reference)
    def perform_create(self, serializer) -> (None):
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
        validated_data = {}

        username = data.get('name')
        email = data.get('email')
        password1 = data.get('password1')
        password2 = data.get('password2')

        validated_data['name'] = []
        validated_data['name'].append(username)

        validated_data['email'] = []
        validated_data['email'].append(email)

        validated_data['paassword'] = []
        validated_data['paassword'].append(password1)

        #? the user technically does not exist currently but we must check that the information provided does meet certain criteria
        if models.Users.objects.filter(name=username).exists():
            validated_data['name'].append("Username already exists.")
            raise serializers.ValidationError("Username already exists")

        if models.Users.objects.filter(name=username, email=email).exists():
            validated_data['email'].append("Username or email adddress incorrect")
            raise serializers.ValidationError("Username or email adddress incorrect")

        if not re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", email):
            validated_data['email'].append("Invalid email address")
            raise serializers.ValidationError("Invalid email address")

        if password1 != password2:
            validated_data['paassword'].append("Password1 and Password2 do not match.")
            raise serializers.ValidationError("Password1 and Password2 do not match")

        if len(password1) < 8:            
            validated_data['paassword'].append("Password must be at least 8 characters long.")

        return validated_data


    def create(self, validated_data) -> (object or None):

        print("\n This is validated data ", validated_data, "\n")

        user = models.User.objects.create(
            username=validated_data['name'][0],
            email=validated_data['email'][0],
            password=validated_data['paassword'][0]
        )

        return user


    def perform_create(self, serializer) -> (None):
        print("Validated data: ", serializer.validated_data)
        if serializer.validated_data == []:
            print("\nINFORMATION MUSN'T BE EMPTY!\n")
            return False
        user = self.create(serializer.validated_data)

        users = models.Users.objects.create(
            user=user,
            name=user.username,
            email=user.email,
            password1=user.password,
            password2=user.password
        )

        user.save
        users.save

        return True




