from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name = 'login'),
    path('registration/', views.UserRegistationView.as_view(), name='registration'),
    path('logout/', views.logout, name='logout'),
]