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


# @login_required
def users_profiles(request, user_id):
    # form = UserProfileForm()
    users = get_object_or_404(User, id=user_id)
    user_profile = get_object_or_404(UserProfile, user_id=user_id)
    resume_exists = bool(user_profile.resume)
    context = {
        'users': users,
        # 'form': form,
        'resume_exists': resume_exists,
        'user_profile': user_profile,
        'user': request.user,
    }
    return render(request, 'homagram_app/users_profiles.html', context)

@login_required
def edit_profile(request):
    user = request.user

    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=user)

    # try:
    #     social_media_links = SocialMediaLink.objects.get(user=user)
    # except SocialMediaLink.DoesNotExist:
    #     social_media_links = SocialMediaLink(user=user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        # social_media_form = SocialMediaLinkForm(request.POST, instance=social_media_links)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'you profile was successfully updated!')
            return redirect('homagram_app:users_profiles')
        else:
            messages.error(request, 'error')
    else:
        profile_form = UserProfileForm(instance=user_profile)

    context = {
        'forms':
            [profile_form,
             # social_media_form,
             ]
    }

    return render(request, 'homagram_app/edit_profile.html', context)


def inner_page(request):
    return render(request, 'homagram_app/inner-page.html')


def feed_page(request):
    form = UserForm()
    users = User.objects.filter(is_superuser=False)

    context = {'form': form,
               'users': users,
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


@login_required
def upload_resume(request):
    if request.method == 'POST':
        resume = request.FILES.get('resume')
        if resume:
            request.user.userprofile.resume = resume
            request.user.userprofile.save()
            return redirect('homagram_app:users_profiles', user_id=request.user.id)
    return render(request, 'homagram_app/upload_resume.html')
