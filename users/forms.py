from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import User
from .choices import GenderChoices


class LoginForm(forms.Form):
    email = forms.CharField(label="email", widget=forms.EmailInput(attrs={'class': "input100",
                                                                          'id': 'email',
                                                                          "placeholder": "Email",
                                                                          "type": "email",
                                                                          "name": "email"}))

    password = forms.CharField(label="password", widget=forms.PasswordInput(attrs={'class': "input100",
                                                                                   'id': 'password',
                                                                                   "type": "password",
                                                                                   "name": "password",
                                                                                   'placeholder': 'Password'}))


class CreateUserForm(forms.ModelForm):
    SEX_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'id': 'password1',
                                                                  'placeholder': 'Password'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'id': 'password2',
                                                                  'placeholder': 'Confirm Password'}))

    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'input100', 'placeholder': 'Email',
                                                           'id': 'email'}))

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100',
                                                             'placeholder': 'Username',
                                                             'id': 'username'}), required=False)

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100',
                                                               'placeholder': 'First Name',
                                                               'id': 'first_name'}))

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100',
                                                              'placeholder': 'Last Name',
                                                              'id': 'last_name'}))

    mobile_number = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'input100',
                                                                     'placeholder': 'Phone',
                                                                     'id': 'mobile_number',
                                                                     'minlength': '9', 'maxlength': '9'}))

    about = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100',
                                                          'id': 'about',
                                                          'placeholder': 'About'}))

    gender = forms.ChoiceField(choices=GenderChoices.choices(), widget=forms.Select(attrs={'class': 'input100',
                                                                                           'id': 'sex',
                                                                                           'placeholder': 'Select you gender',
                                                                                           }))

    age = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'input100',
                                                           'placeholder': 'Age',
                                                           'id': 'age',
                                                           }))

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'password1', 'password2',
            'mobile_number',
            'about',
            'gender',
            'age',
        )

        exclude = ('is_active', 'is_staff', 'date_joined', 'permission', 'password')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    #
    # def clean_phone(self, *args, **kwargs):
    #     mobile_number = self.cleaned_data.get('phone')
    #     if not mobile_number.isdigit():
    #         raise forms.ValidationError('You must input valid phone number!')
    #     else:
    #         return mobile_number
    #
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        print('register user form save---------------------------------')
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(label='current_password',
                                       widget=forms.PasswordInput(attrs={'class': "input100",
                                                                         'id': 'password1',
                                                                         "type": "password",
                                                                         "name": "password",
                                                                         'placeholder': 'Current Password',
                                                                         }))
    password = forms.CharField(label='new_password', widget=forms.PasswordInput(attrs={'class': "input100",
                                                                                       'id': 'password2',
                                                                                       "type": "password",
                                                                                       "name": "password",
                                                                                       'placeholder': 'New Password',
                                                                                       }))
    repeat_password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': "input100",
                                                                                          'id': 'password3',
                                                                                          "type": "password",
                                                                                          "name": "password",
                                                                                          'placeholder': 'Repeat Password',
                                                                                          }))


class ResetForgotPasswordForm(forms.Form):
    password = forms.CharField(label='new_password', widget=forms.PasswordInput(attrs={'class': "input100",
                                                                                       'id': 'password',
                                                                                       "type": "password",
                                                                                       "name": "password",
                                                                                       'placeholder': 'New Password',
                                                                                       }))
    repeat_password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': "input100",
                                                                                          'id': 'password',
                                                                                          "type": "password",
                                                                                          "name": "password",
                                                                                          'placeholder': 'Repeat Password',
                                                                                          }))

    email = forms.CharField(label='email', widget=forms.EmailInput(attrs={'class': "input100",
                                                                          'id': 'email',
                                                                          'type': 'email',
                                                                          'name': 'email',
                                                                          'placeholder': 'Email',
                                                                          }))
