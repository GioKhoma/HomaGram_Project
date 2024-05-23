from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_forgot_password/', views.reset_forgot_password, name='reset_forgot_password'),
]