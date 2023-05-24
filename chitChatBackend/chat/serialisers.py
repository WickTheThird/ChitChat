from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class Users(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Users
        fields = ("name", "email", "password1", "password2")
