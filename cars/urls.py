from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from cars import views

app_name = 'cars'

urlpatterns = [
    path('', views.cars, name='cars'),
    path('search/', views.search_car, name='search_car'),
]