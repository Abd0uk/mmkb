from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return render(request, 'home.html')


def login_user(request):
    # check if the user is logging in
    if request.method == 'POST':
        # Safely get username and password
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:  # Ensure both fields are provided
            # authenticate
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have been logged in!')
                return redirect('core:home')
            else:
                messages.error(request, 'Invalid username or password. Please try again.') 
        else:
            messages.error(request, 'Both username and password are required.')

        return redirect('core:login')
    
    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "you have been logged out")
    return redirect('core:login')