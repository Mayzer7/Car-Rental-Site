from django.contrib import admin
from .models import Car, RareCar


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'mileage', 'year', 'transmission', 'location', 'car_type', 'price')
    list_filter = ('year', 'brand', 'car_type', 'transmission')
    search_fields = ('name', 'brand', 'location')

@admin.register(RareCar)
class RareCarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'mileage', 'year', 'transmission', 'location', 'car_type', 'price')
    list_filter = ('year', 'brand', 'car_type', 'transmission')
    search_fields = ('name', 'brand', 'location')   