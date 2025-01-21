from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.cars, name='cars'),
]