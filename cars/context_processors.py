from .models import Car, RareCar

def all_cars(request):
    cars = Car.objects.all()  # Или используйте фильтры для последних автомобилей
    unique_brands = {car.brand for car in cars if car.brand} # Уникальные бренды
    unique_model = {car.model for car in cars if car.model}  
    unique_location = {car.location for car in cars if car.location}  
    unique_year = {car.year for car in cars if car.year}
    unique_car_type = {car.car_type for car in cars if car.car_type}  
    return {
        'all_cars': cars, 
        'unique_brands': sorted(unique_brands),
        'unique_model': sorted(unique_model),
        'unique_location': sorted(unique_location),
        'unique_year': sorted(unique_year),
        'unique_car_type': sorted(unique_car_type)
    } 

def rare_cars(request):
    cars = RareCar.objects.all()  # Или используйте фильтры для последних автомобилей
    # unique_brands = {car.brand for car in cars if car.brand} # Уникальные бренды
    # unique_model = {car.model for car in cars if car.model}  
    # unique_location = {car.location for car in cars if car.location}  
    # unique_year = {car.year for car in cars if car.year}
    # unique_car_type = {car.car_type for car in cars if car.car_type}  
    return {
        'rare_cars': cars, 
        # 'unique_brands': sorted(unique_brands),
        # 'unique_model': sorted(unique_model),
        # 'unique_location': sorted(unique_location),
        # 'unique_year': sorted(unique_year),
        # 'unique_car_type': sorted(unique_car_type)
    }

