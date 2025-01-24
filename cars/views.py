from django.shortcuts import render
from django.shortcuts import render
from .models import Car
from .forms import CarSearchForm
from django.db.models import Q


def cars(request):
    return render(request, 'cars/cars.html')

def search_car(request):
    # Получаем параметры из формы
    keyword = request.GET.get('keyword')
    brand = request.GET.get('select-brand')
    model = request.GET.get('select-make')
    location = request.GET.get('select-location')
    year = request.GET.get('select-year')
    car_type = request.GET.get('select-type')
    min_price = request.GET.get('min_price')  # Минимальная цена
    max_price = request.GET.get('max_price')  # Максимальная цена

    # Начинаем с общего набора всех машин
    cars = Car.objects.all()

    # Фильтруем по каждому параметру, если он указан
    if keyword:
        cars = cars.filter(name__icontains=keyword)
    if brand:
        cars = cars.filter(brand__icontains=brand)
    if model:
        cars = cars.filter(model__icontains=model)
    if location:
        cars = cars.filter(location__icontains=location)
    if year:
        cars = cars.filter(year=year)
    if car_type:
        cars = cars.filter(car_type=car_type)
    if min_price and max_price:
        cars = cars.filter(price__gte=min_price, price__lte=max_price)

    # Проверяем, найдены ли машины
    if cars.exists():
        return render(request, 'cars/car_found.html', {'cars': cars})
    else:
        return render(request, 'cars/car_not_found.html')