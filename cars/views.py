from django.shortcuts import render
from .models import Car
from django.db.models import Q
from django.core.paginator import Paginator

def cars(request):
    return render(request, 'cars/cars.html')

def search_car(request):
    # Получение фильтров из GET-запроса
    keyword = request.GET.get('keyword', '')
    brand = request.GET.get('select-brand', '')
    model = request.GET.get('select-make', '')
    location = request.GET.get('select-location', '')
    year = request.GET.get('select-year', '')
    car_type = request.GET.get('select-type', '')

    # Основной запрос
    cars = Car.objects.all()

    # Применение фильтров
    if keyword:
        cars = cars.filter(name__icontains=keyword)
    if brand:
        cars = cars.filter(brand__icontains=brand)
    if model:
        cars = cars.filter(model__icontains=model)
    if location:
        cars = cars.filter(location__icontains=location)
    if year:
        cars = cars.filter(year__icontains=year)
    if car_type:
        cars = cars.filter(car_type__icontains=car_type)


    # Проверка, есть ли результаты
    if not cars.exists():
        message = "Автомобиль с указанными критериями не найден. Показан весь список автомобилей."
        cars = Car.objects.all()  # Возвращаем все автомобили
    else:
        message = ""

    # Пагинация
    paginator = Paginator(cars, 4)  # 4 автомобилей на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Передача текущих фильтров в контекст
    return render(request, 'cars/car_found.html', {
        'page_obj': page_obj,
        'message': message,
        'filters': {
            'keyword': keyword,
            'brand': brand,
            'model': model,
            'location': location,
            'year': year,
            'car_type': car_type,
        },
    })