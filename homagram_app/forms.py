from django import forms
from users.models import User
from .models import UserProfile, SocialMediaLink


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'


class SocialMediaLinkForm(forms.ModelForm):
    class Meta:
        model = SocialMediaLink
        fields = '__all__'
