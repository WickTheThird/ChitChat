from django.shortcuts import  render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

#? INDEX
def index(request):
    return render(request, 'login.html')

# REGISTER
def registerRequest(request):

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful." )
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})


# LOGIN
def loginRequest(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

# LOGOUT
def logoutRequest(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("login")

#> HOME
@login_required
def home(request):

    currentUser = request.user
    try:
        currentUser.customer
    except Customer.DoesNotExist:
        Customer.objects.create(id=currentUser, name=currentUser.username, email=currentUser.email)
        
    friendRequests = FriendRequests.objects.filter(receiver=currentUser.customer)
        
    if request.method == 'POST':

        if "search" in request.POST:
            userName = request.POST["search"]
            customer = Customer.objects.filter(name__icontains=userName)

            if len(customer) > 0:
                customer = customer[0] #? username is unique

            if customer and customer.name != currentUser.username:
                return render(request, 'home.html', {
                                                        'customer': customer,
                                                        'friendRequests': friendRequests,
                                                    })

    return render(request, 'home.html', {'friendRequests': friendRequests})

#> USER PROFILE // will work on this a more later on
@login_required
def user(request, userName):
    user = Customer.objects.filter(name__icontains=userName)
    
    if len(user) > 0:
        user = user[0] #? username is unique
    
    return render(request, 'user.html', {'user': user})

#> FRIEND REQUEST
@login_required
def sendFriendRequest(request, userName):
    whichUser = Customer.objects.filter(name__icontains=userName)

    if len(whichUser) > 0:
        whichUser = whichUser[0] #? username is unique

    currentUser = request.user.customer

    if currentUser != whichUser:
        FriendRequests.objects.create(sender=currentUser, receiver=whichUser, state=True)

    return redirect("home")

#todo: make sure that in this model, the senders and recivers are added to each others friend fields...
def acceptFriendRequest(request, userName):

    whichUser = Customer.objects.filter(name__icontains=userName)
    
    if len(whichUser) > 0:
        whichUser = whichUser[0] #? username is unique
    
    req = FriendRequests.objects.filter(sender=whichUser, receiver=request.user.customer)

    #? Note that a user may have multiple requests from the same person...
    for r in req:
        r.receiver=None
        r.sender=None
        r.state=False
        r.save()

    return redirect("home")

def declineFriendRequest(request, userName):

    whichUser = Customer.objects.filter(name__icontains=userName)

    if len(whichUser) > 0:
        whichUser = whichUser[0] #? username is unique

    req = FriendRequests.objects.filter(sender=whichUser, receiver=request.user.customer)
    
    #? Note that a user may have multiple requests from the same person...
    for r in req:
        print("Was", r.receiver, r.sender, r.state)
        r.receiver=None
        r.sender=None
        r.state=False
        print("Should be", r.receiver, r.state, r.state)
        r.save()

    return redirect("home")

def deleteRequest(request, userName):

    whichUser = Customer.objects.filter(name__icontains=userName)

    if len(whichUser) > 0:
        whichUser = whichUser[0] #? username is unique

    req = FriendRequests.objects.filter(sender=whichUser, receiver=request.user.customer)

    #? Reject/accept once means all requests are deleted
    for r in req:
        r.delete()

    return render("home")
