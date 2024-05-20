from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout

@login_required
def index(request):
    # form = CreateUserForm()
    #
    # context = {'form': form}
    return render(request, 'users/index.html', {'user': request.user})


def registration(request):
    form = CreateUserForm()
    print('get method')

    if request.method == 'POST':
        print('post method')
        form = CreateUserForm(request.POST, request.FILES)
        print('form instantiated')
        if form.is_valid():
            print('form is valid')
            form.save()
            # data = form.save(commit=False)
            # data.save()
            print('data saved')

            return redirect('users:login')
        else:
            print('form is invalid')

    context = {'form': form}

    return render(request, 'users/registration.html', context)


User = get_user_model()


def my_login(request):
    form = LoginForm()
    print('get method')

    if request.method == 'POST':
        print('post method')
        form = LoginForm(request.POST)
        print('form instantiated')

        if form.is_valid():
            # email = request.POST.get('email')
            # password = request.POST.get('password')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            print('form is valid')

            # uses the authenticate function to check if username and password matches, if they matches it returns None
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                print('user logged in')
                # uses login function and creating a session

                # auth.login(request, user)

                return redirect('users:index')
            else:
                print('invaild username or password')

    context = {'form': form}

    return render(request, 'users/login.html', context)


def my_logout(request):
    logout(request)
    return redirect('users:login')
