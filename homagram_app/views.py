from django.shortcuts import render, redirect, HttpResponse
# from users.forms import CreateUserForm
# from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from users.models import User
from .models import UserProfile, SocialMediaLink
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from homagram import settings
from django.http import JsonResponse
from .forms import UserForm, UserProfileForm, SocialMediaLinkForm
from django.shortcuts import get_object_or_404
from django.contrib import messages


@login_required
def users_profiles(request, user_id):
    user_profile = get_object_or_404(UserProfile, user_id=user_id)
    form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
    users = get_object_or_404(User, id=user_id)
    resume_exists = bool(user_profile.resume)

    if request.method == 'POST':
        resume = request.FILES.get('resume')
        if resume:
            request.user.userprofile.resume = resume
            request.user.userprofile.save()
            return redirect('homagram_app:users_profiles', user_id=request.user.id)

    context = {
        'users': users,
        'form': form,
        'resume_exists': resume_exists,
        'user_profile': user_profile,
        'user': request.user,
    }
    return render(request, 'homagram_app/users_profiles.html', context)


@login_required
def edit_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            if 'resume' in request.FILES:
                user_profile.resume = request.FILES['resume']
            form.save()
            return redirect('homagram_app:users_profiles', user_id=user_profile.user_id)
    else:
        form = UserProfileForm(instance=user_profile)

    context = {'form': form,
               'user_profile': user_profile,
               }
    return render(request, 'homagram_app/edit_profile.html', context)


def inner_page(request):
    return render(request, 'homagram_app/inner-page.html')


def feed_page(request):
    form = UserForm()
    users = User.objects.filter(is_superuser=False)
    user_profile = get_object_or_404(UserProfile, user=request.user)

    context = {'form': form,
               'users': users,
               'user_profile': user_profile
               }
    return render(request, 'homagram_app/feed_page.html', context)


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
            ['YOUR_EMAIL_GOES_HERE']
        )

        email.fail_silently = False
        email.send()

        return JsonResponse({'status': 'success'})

    return render(request, 'homagram_app/users_profiles.html')


def delete_resume(request):
    # remove_resume = UserProfile.objects.get(id=resume_id)
    user_profile = get_object_or_404(UserProfile, user=request.user.userprofile)
    print('user_profile geeet')
    if request.method == 'POST':
        print('pooost')
        user_profile.resume = None
        print('nonee')
        user_profile.save()
        print('saved')

        # remove_resume.resume.delete()
        return redirect('hoamgram_app:edit_profile')

    context = {
        # 'remove_resume': remove_resume,
        'user_profile': user_profile,
    }

    return render(request, 'homagram_app/edit_profile.html', context)

#
# def delete_factories(request, factory_id):
#     factory = DeliveryAddress.objects.get(id=factory_id)
#
#     if request.method == 'POST':
#         factory.delete()
#         return redirect('customer_profile:customerFactories')
#
#     context = {'factory': factory}
#     return render(request, 'customer_profile/customer_factories.html', context)
