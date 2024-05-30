from django.db import models
from users.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True, default=None)
    age = models.IntegerField(blank=True, null=True)
    phone = models.IntegerField(unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    title_about_text = models.CharField(max_length=50,blank=True, null=True)
    about_text = models.CharField(max_length=1200, blank=True, null=True)
    profile_photo = models.ImageField(null=True, blank=True, upload_to='img/profile_img', default='img/default_img.jpg')
    about_facts = models.CharField(max_length=100, blank=True, null=True)
    happy_clients = models.IntegerField(default=0)
    projects = models.IntegerField(default=0)
    hours_of_support = models.IntegerField(default=0)
    hard_worker = models.IntegerField(default=0)
    location = models.CharField(max_length=40, blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    resume_text = models.CharField(max_length=100, blank=True, null=True)
    pers_website = models.URLField(max_length=200, blank=True, null=True)
    degree = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} - Profile"


class SocialMediaLink(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    skype_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} - Social Media Links"
