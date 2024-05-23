from django.urls import path
from . import views

app_name = 'homagram_app'

urlpatterns = [
    path('profile/', views.index, name='index'),
    path('feed_page/', views.feed_page, name='feed'),
    path('send_email/', views.send_email, name='send_email'),
    # path('portf/', views.portfolio_details, name='portfolio_details'),
]