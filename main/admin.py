from django.contrib import admin
from .models import Person

@admin.register(Person)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'post')
    list_filter = ('name', 'post')
    search_fields = ('name', 'post')
