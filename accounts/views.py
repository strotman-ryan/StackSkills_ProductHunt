from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def SignUp(request):
    if request.method == 'POST':
        # user wants an account now
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username is already in use'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],None,request.POST['password2'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'passwords must match'})
    else:
        #user wants to enter info
        return render(request, 'accounts/signup.html')
    

def LogIn(request):
    if request.method == 'POST':
        user = auth.authenticate(username =request.POST['username'] , password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def LogOut(request):
    #TODO: Need to route to home page
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')