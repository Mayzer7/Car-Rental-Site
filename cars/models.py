from PIL import Image
from django.db import models

# Основная модель автомобиля
class Car(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название машины")
    brand = models.CharField(max_length=20, null=True, blank=True, verbose_name="Брэнд")
    model = models.CharField(max_length=255, null=True, blank=True, verbose_name="Модель")
    mileage = models.PositiveIntegerField(verbose_name="Пробег (в км)")
    year = models.PositiveIntegerField(verbose_name="Год выпуска")
    transmission = models.CharField(max_length=50, verbose_name="Привод", choices=(
        ('ППР', 'Полный привод'),
        ('ПП', 'Передний привод'),
        ('ЗП', 'Задний привод'),
    ))
    location = models.CharField(max_length=255, verbose_name="Адрес")
    car_type = models.CharField(max_length=50, verbose_name="Класс автомобиля", choices=(
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('truck', 'Truck'),
        ('coupe', 'Coupe')
    ))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена аренды")
    image = models.ImageField(upload_to='cars/', verbose_name="Изображение (750x500px)")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Сохраняем объект
        self.resize_image(self.image)

    def resize_image(self, image_field):
        """Масштабирование изображения до 750x500px"""
        if image_field:
            img = Image.open(image_field.path)
            img = img.resize((750, 500), Image.Resampling.LANCZOS)
            img.save(image_field.path)

    class Meta:
        verbose_name = "машину"
        verbose_name_plural = "Все машины"

    def __str__(self):
        return self.name

class RareCar(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название машины")
    brand = models.CharField(max_length=20, null=True, blank=True, verbose_name="Брэнд")
    model = models.CharField(max_length=255, null=True, blank=True, verbose_name="Модель")
    mileage = models.PositiveIntegerField(verbose_name="Пробег (в км)")
    year = models.PositiveIntegerField(verbose_name="Год выпуска")
    transmission = models.CharField(max_length=50, verbose_name="Привод", choices=(
        ('ППР', 'Полный привод'),
        ('ПП', 'Передний привод'),
        ('ЗП', 'Задний привод'),
    ))
    location = models.CharField(max_length=255, verbose_name="Адрес")
    car_type = models.CharField(max_length=50, verbose_name="Класс автомобиля", choices=(
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('truck', 'Truck'),
        ('coupe', 'Coupe')
    ))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена аренды")
    image = models.ImageField(upload_to='cars/', verbose_name="Изображение (750x500px)")

     # Поля для дополнительных изображений
    additional_image_1 = models.ImageField(upload_to='cars/additional_images/', null=True, blank=True, verbose_name="Дополнительное изображение 1")
    additional_image_2 = models.ImageField(upload_to='cars/additional_images/', null=True, blank=True, verbose_name="Дополнительное изображение 2")
    additional_image_3 = models.ImageField(upload_to='cars/additional_images/', null=True, blank=True, verbose_name="Дополнительное изображение 3")
    additional_image_4 = models.ImageField(upload_to='cars/additional_images/', null=True, blank=True, verbose_name="Дополнительное изображение 4")
    additional_image_5 = models.ImageField(upload_to='cars/additional_images/', null=True, blank=True, verbose_name="Дополнительное изображение 5")

    # Поле связи с Car
    car_ref = models.OneToOneField(Car, on_delete=models.CASCADE, null=True, blank=True, related_name="rare_car")

    def save(self, *args, **kwargs):
        """Создаёт или обновляет Car, избегая NULL-значений"""
        if not self.car_ref:
            # Если car_ref нет, создаём новый Car
            car = Car.objects.create(
                name=self.name,
                brand=self.brand,
                model=self.model,
                mileage=self.mileage,
                year=self.year,
                transmission=self.transmission,
                location=self.location,
                car_type=self.car_type,
                price=self.price,
                image=self.image
            )
            self.car_ref = car  # Связываем RareCar с Car
        else:
            # Если car_ref есть, обновляем его
            car = self.car_ref
            car.name = self.name
            car.brand = self.brand
            car.model = self.model
            car.mileage = self.mileage
            car.year = self.year
            car.transmission = self.transmission
            car.location = self.location
            car.car_type = self.car_type
            car.price = self.price
            car.image = self.image
            car.save()

        super().save(*args, **kwargs)  # Сохраняем RareCar с обновлённой ссылкой

    def delete(self, *args, **kwargs):
        """При удалении RareCar удаляем и его копию в Car"""
        if self.car_ref:
            self.car_ref.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "редкую машину"
        verbose_name_plural = "Редкие машины"

    def __str__(self):
        return self.name
