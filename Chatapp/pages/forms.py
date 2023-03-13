import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.timezone import datetime 
from .models import *

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super(NewUserForm, self).clean()
        error  = []

        # SIGNUP DETAILS
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        # VALIDATION
        if User.objects.filter(username=username).exists():
            error.append('Username already exists')

        if User.objects.filter(email=email).exists():
            error.append('Email already exists')

        if not re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", email):
            error.append('Invalid email address')

        if password1 != password2:
            error.append('Passwords do not match')

        if error:
            raise forms.ValidationError(error)



