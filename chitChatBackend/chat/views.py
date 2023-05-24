from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request=request, template_name='index.html')

#> Entry Form
def login(request, username, useremail): #todo -> it would be better if the information would be stored in the request itself via json
    from . import validator

@login_required
def logout(request, username): #todo -> it would be better if the information would be stored in the request itself via json
    from . import validator

def signup(request, username, useremail): #todo -> we need to add a new user to the Users model, once signed up
                     #todo -> proper validation needs to be added, for the form 
                     #     -> since the form is on the frontend side and the signup us a request
                     #     -> we need just to validate data and return a response on wether data
                     #     -> has been added to the database or not, thus proper validators need to be created
    from . import validator
