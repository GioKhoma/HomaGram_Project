from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.core.validators import validate_email


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password=None,
                     # username,
                     # first_name,
                     # last_name, mobile_number, about,
                     **extra_fields):
        print('register user model save---------------------------------')
        validate_email(email)
        email = self.normalize_email(email)
        user = self.model(email=email,
                          # username=username,
                          # first_name=first_name,
                          # last_name=last_name,
                          # mobile_number=mobile_number,
                          # about=about,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email,
                    # username,
                    # first_name, last_name, mobile_number,
                    # about,
                    password=None,
                    **extra_fields):
        print('register user model save---------------------------------')
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password,
                                 # username,
                                 # first_name, last_name, mobile_number,
                                 # about,
                                 **extra_fields)

    def create_superuser(self, email,
                         # username,
                         # first_name,
                         # last_name,
                         # mobile_number,
                         # about,
                         password=None,
                         **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password,
                                 # username=username,
                                 # first_name='super',
                                 # last_name='user',
                                 # mobile_number='',
                                 # about='',
                                 **extra_fields)


# profile_picture, username, email, first_name, last_name, mobile_number, about, sex

class User(AbstractUser):
    profile_picture = models.ImageField(null=True, blank=True, upload_to='img/', default='default_img.jpg')
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=20)
    about = models.CharField(max_length=250)
    # permission = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # date_joined = models.DateTimeField(default=timezone.now)

    MALE = 'Male'
    FEMALE = 'Female'
    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    sex = models.CharField(
        max_length=6,
        choices=SEX_CHOICES,
        blank=True,
        null=True,
        default=None,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
