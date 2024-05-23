from django.shortcuts import render, redirect, HttpResponse
# from users.forms import CreateUserForm
# from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from users.models import User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from homagram import settings
from django.http import JsonResponse


@login_required
def index(request):
    # form = UserProfileForm()
    users = User.objects.get(first_name=request.user.first_name, last_name=request.user.last_name)

    context = {'users': users,
               # 'form': form,
               'user': request.user,
               }
    return render(request, 'homagram_app/index.html', context)


def inner_page(request):
    return render(request, 'homagram_app/inner-page.html')


def feed_page(request):
    return render(request, 'homagram_app/feed_page.html')


def send_email(request):
    if request.method == 'POST':
        template = render_to_string('homagram_app/email_template.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message']
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['emailsender1432@gmail.com']
        )

        email.fail_silently = False
        email.send()

        return JsonResponse({'status': 'success'})

    return render(request, 'homagram_app/index.html')




