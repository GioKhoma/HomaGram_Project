from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect, HttpResponse
from .forms import CreateUserForm, LoginForm, ChangePasswordForm, ResetForgotPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail


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

            # user = form.save()
            # profile_picture = form.cleaned_data.get('profile_picture')
            # if profile_picture:
            #     user_profile = User(user=user, profile_picture=profile_picture)
            #     user_profile.save()

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
    # print('get method')

    if request.method == 'POST':
        # print('post method')
        form = LoginForm(request.POST)
        # print('form instantiated')

        if form.is_valid():
            # email = request.POST.get('email')
            # password = request.POST.get('password')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            # print('form is valid')

            # uses the authenticate function to check if username and password matches, if they matches it returns None
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                # print('user logged in')
                # uses login function and creating a session

                # auth.login(request, user)

                return redirect('homagram_app:feed')
            else:
                print('invaild username or password')

    context = {'form': form}

    return render(request, 'users/login.html', context)


def my_logout(request):
    logout(request)
    return redirect('users:login')


@login_required
def change_password(request):
    form = ChangePasswordForm()
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)

        if request.user.check_password(request.POST.get('current_password')):
            if form.is_valid():
                user.set_password(str(form.cleaned_data['password']))
                user.save()
                logout(request)
                messages.info(request, "პაროლი წარმატებით განახლდა!")
                return redirect('users:login')

    context = {'form': form,
               'user': user
               }
    return render(request, 'users/change_password.html', context)


def send_email(email):
    user = User.objects.get(email=email)
    token = default_token_generator.make_token(user)
    reset_url = f"http://127.0.0.1:8000/reset_forgot_password/?email={email}&token={token}"

    subject = "პაროლის აღდგენა"
    message = f'პაროლის გასაახლებლად გთხოვთ გადახვიდეთ ლინკზე: {reset_url}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if User.objects.filter(email=email).exists():
            send_email(email)
            messages.info(request, "იემილი წარმატებით გაიგზავნა!")

        else:
            messages.info(request, "აღნიშნულ მეილზე აქაუნთი არ არის რეგისტრირებული.")

    return render(request, 'users/forgot_password.html')


def reset_forgot_password(request):
    form = ResetForgotPasswordForm()

    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        form = ResetForgotPasswordForm(request.POST)

        if form.is_valid():
            if str(form.cleaned_data['password']) == str(form.cleaned_data['repeat_password']):
                user.set_password(str(form.cleaned_data['password']))
                user.save()
                logout(request)
                messages.info(request, "პაროლი წარმატებით განახლდა!")
                return redirect('users:login')

    context = {
        'form': form,
    }

    return render(request, 'users/reset_forgot_password.html', context)



