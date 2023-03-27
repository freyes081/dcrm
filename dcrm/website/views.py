from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    #Check if user is loggin in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Autenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return render(request, 'home.html')
        else:
            messages.success(request, 'Invalid credentials')
            return render(request, 'home.html')
    else:
        return render(request, 'home.html')



def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logout...')
    return redirect('home')

def register_user(request):
   return render(request, 'register.html')


