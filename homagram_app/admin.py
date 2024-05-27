from django.contrib import admin
from .models import UserProfile, SocialMediaLink

admin.site.register(UserProfile)

admin.site.register(SocialMediaLink)
