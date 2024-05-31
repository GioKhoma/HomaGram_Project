from django import forms
from users.models import User
from .models import UserProfile, SocialMediaLink


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class UserProfileForm(forms.ModelForm):
    resume = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': "input100"}))

    class Meta:
        model = UserProfile
        fields = [
            'birth_date', 'age', 'phone', 'email', 'about_text',
            'profile_photo', 'about_facts', 'happy_clients', 'projects',
            'hours_of_support', 'hard_worker', 'location', 'resume',
            'title_about_text', 'resume_text', 'pers_website', 'degree',
        ]

        widgets = {
            'birth_date': forms.DateInput(attrs={'class': "input100", 'placeholder': 'YYYY-MM-DD'}),
            'age': forms.NumberInput(attrs={'class': "input100", 'placeholder': 'Enter your age'}),
            'phone': forms.NumberInput(attrs={'class': "input100", 'placeholder': 'Enter phone number'}),
            'email': forms.EmailInput(attrs={'class': "input100", 'placeholder': 'Enter your email'}),
            'about_text': forms.TextInput(attrs={'class': "input100", 'placeholder': 'Tell us about yourself'}),
            'profile_photo': forms.FileInput(attrs={'class': 'input100'}),
            'about_facts': forms.TextInput(attrs={'class': "input100", 'placeholder': 'Facts about you'}),
            'happy_clients': forms.NumberInput(attrs={'class': "input100", 'placeholder': 'Amount of clients'}),
            'projects': forms.NumberInput(attrs={'class': "input100", 'placeholder': 'Amount of projects'}),
            'hours_of_support': forms.NumberInput(attrs={'class': "input100", 'placeholder': 'Amount of hours'}),
            'hard_worker': forms.NumberInput(attrs={'class': "input100", 'placeholder': 'Amount of hard worker'}),
            'location': forms.TextInput(attrs={'class': "input100", 'placeholder': 'Your location'}),
            # 'resume': forms.FileInput(attrs={'class': "input100"}),
            'title_about_text': forms.TextInput(attrs={'class': "input100", 'placeholder': 'Title of about text'}),
            'resume_text': forms.TextInput(attrs={'class': "input100", 'placeholder': 'Title of resume'}),
            'pers_website': forms.TextInput(attrs={'class': "input100", 'placeholder': 'Personal website link'}),
            'degree': forms.TextInput(attrs={'class': "input100", 'placeholder': 'Your degree'}),
        }


class SocialMediaLinkForm(forms.ModelForm):
    class Meta:
        model = SocialMediaLink
        fields = '__all__'


