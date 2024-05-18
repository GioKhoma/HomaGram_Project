from django.shortcuts import render, redirect, HttpResponse
from .forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout



def index(request):
    return render(request, 'users/index.html')


def registration(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('login')

    context = {'form': form}

    return render(request, 'users/registration.html', context)


def my_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            # uses the authenticate function to check if username and password matches, if they matches it returns None
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # uses login function and creating a session

                auth.login(request, user)

                return redirect('dashboard')

    context = {'form': form}

    return render(request, 'users/login.html', context)
