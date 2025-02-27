from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.
def signup_view(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        if(User.objects.filter(username=username).exists()):
            messages.error(request, "Username is already taken!")
            return redirect('signup')
        user=User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Successfully signed up, Please login...")
        return redirect('login')
    return render(request, 'signup.html')

def login_view(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credential!")
    return render(request, 'login.html')

