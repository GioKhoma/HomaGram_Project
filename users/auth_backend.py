# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model
# from django.core.exceptions import ValidationError
#
# User = get_user_model()
#
#
# class CustomModelBackend(ModelBackend):
#     def authenticate(self, request, email=None, password=None, **kwargs):
#         # if email in None or password in None:
#         #     return ValidationError('email or password is incorrect')
#
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             return None
#
#         if user.check_password(password):
#             return user
#         return None
#
#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None


from typing import Any
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http import HttpRequest
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class CustomModelBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        print('authenticate test 1')
        # if not kwargs.get("call_type"):
        if username is None or password is None:
            print('authenticate test 1-1', username, password)
            return
        print('authenticate test 1-2', username, password)

        try:
            print('authenticate test 2')
            user = UserModel._default_manager.get_by_natural_key(username)
            print('authenticate test 3', user)
        except UserModel.DoesNotExist:
            print('authenticate test 4')
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            # if kwargs.get("call_type") == "api":
            #     return user
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

        return super().authenticate(request, username, password, **kwargs)

