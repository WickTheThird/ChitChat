from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import forms

def index(request):
    return render(request=request, template_name='index.html')

#> Entry Form
def loginRequest(request, username, useremail): #todo -> it would be better if the information would be stored in the request itself via json
    from . import validator

    if request.method == "GET":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid(): #todo -> we need to change the form is valid to the valid file inside the validator.py (note that if it doesn't affect it then call the validator later)
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password, email=useremail)
            
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")

                return True #> Returns a state that will change the frontent

            else:
                messages.error(request, f"Invalid username or password.")
        else:
            messages.error(request, f"Invalid username or password.")

    form = AuthenticationForm()
    return False
                

@login_required
def logoutRequest(request, username): #todo -> it would be better if the information would be stored in the request itself via json
    if request.method == "GET":
        logout(request)
        messages.info(request, f"You have successfully logged out {username}")
        return True

def signupRequest(request, username, useremail): #todo -> we need to add a new user to the Users model, once signed up
                     #todo -> proper validation needs to be added, for the form 
                     #     -> since the form is on the frontend side and the signup us a request
                     #     -> we need just to validate data and return a response on wether data
                     #     -> has been added to the database or not, thus proper validators need to be created
    from . import validator
    
    if request.method == "POST":
        form = forms.NewUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return True

        messages.error(request, "Registration failed.")

    form = forms.NewUserForm()
    return False
