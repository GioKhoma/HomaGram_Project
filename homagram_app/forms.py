from django import forms
from users.models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
