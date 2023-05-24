import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    error = []
    
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = models.Users
        fields = ("name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super(NewUserForm, self).clean()
        self.error = []

        #> SIGNUP DETAILS
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        #> VALIDATION
        if User.objects.filter(username=username).exists():
            self.error.append("Username already exists!")

        if User.objects.filter(email=email).exists():
            self.error.append("Email already exists!")

        if not re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", email):
            self.error.append("Invalid email address!")

        if password1 != password2:
            self.error.append("Passwords do not match!")

        if len(password1) < 8:
            self.error.append("Password is too short!")

        if self.error:
            return self.error
        
        return None
