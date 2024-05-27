from django.urls import path
from . import views

app_name = 'homagram_app'

urlpatterns = [
    path('profile/<int:user_id>/', views.users_profiles, name='users_profiles'),
    path('feed_page/', views.feed_page, name='feed'),
    path('send_email/', views.send_email, name='send_email'),
    path('upload_resume/', views.upload_resume, name='upload_resume'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]