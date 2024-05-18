from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.my_login, name='login'),
    # path('inner/', views.inner_page, name='inner_page'),
    # path('portf/', views.portfolio_details, name='portfolio_details'),
]