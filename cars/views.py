from django.shortcuts import render
from .models import Car
from django.db.models import Q

def cars(request):
    return render(request, 'cars/cars.html')

def search_car(request):
    # Получаем параметры из формы
    keyword = request.GET.get('keyword', '').strip()
    brand = request.GET.get('select-brand', '').strip()
    model = request.GET.get('select-make', '').strip()
    location = request.GET.get('select-location', '').strip()
    year = request.GET.get('select-year', '').strip()
    car_type = request.GET.get('select-type', '').strip()
    
    # Обработка диапазона цен
    try:
        min_price = int(request.GET.get('min_price', 0))
    except (ValueError, TypeError):
        min_price = 0
    
    try:
        max_price = int(request.GET.get('max_price', 150000))
    except (ValueError, TypeError):
        max_price = 150000

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
        cars = cars.filter(car_type__icontains=car_type)
    if min_price is not None and max_price is not None:
        cars = cars.filter(price__gte=min_price, price__lte=max_price)

    # Проверяем, найдены ли машины
    if cars.exists():
        return render(request, 'cars/car_found.html', {'cars': cars})
    else:
        return render(request, 'cars/car_not_found.html')
