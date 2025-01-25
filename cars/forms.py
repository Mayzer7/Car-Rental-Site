from django import forms
from .models import Car

class CarSearchForm(forms.Form):
    name = forms.CharField(required=False, label='Search by name')
    brand = forms.CharField(required=False, label='Brand')
    mileage = forms.IntegerField(required=False, label='Mileage (km)')
    year = forms.IntegerField(required=False, label='Year')
    transmission = forms.ChoiceField(required=False, label='Transmission', choices=Car.transmission.field.choices)
    location = forms.CharField(required=False, label='Location')
    car_type = forms.ChoiceField(required=False, label='Car Type', choices=Car.car_type.field.choices)
    min_price = forms.DecimalField(required=False, label='Min Price')
    max_price = forms.DecimalField(required=False, label='Max Price')

    