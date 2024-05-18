from django.contrib import admin
from .models import User

admin.site.register(User)


# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.utils.translation import gettext_lazy as _
#
# from users.models import User
#
#
# @admin.register(User)
# class UserAdmin(UserAdmin):
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         (_('Personal info'), {'fields': ('username', 'first_name', 'last_name', 'mobile_number', 'about')}),
#         (_('Permissions'), {
#             'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions'),
#         }),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': (
#                 'email', 'password1', 'password2', "first_name", "last_name", "mobile_number", "about", "username"),
#         }),
#     )
#     list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
#     search_fields = ('first_name', 'last_name', 'email',)
#     list_display = ('email', 'first_name', 'last_name',)
#     ordering = ['email']
