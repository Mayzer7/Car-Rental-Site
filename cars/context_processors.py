from .models import Car

def latest_cars(request):
    cars = Car.objects.all()  # Или используйте фильтры для последних автомобилей
    return {'latest_cars': cars}