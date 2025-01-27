from PIL import Image
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название машины")
    brand = models.CharField(max_length=20, null=True, blank=True, verbose_name="Брэнд")
    model = models.CharField(max_length=20, null=True, blank=True, verbose_name="Модель")
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

        def resize_image(image_field):
            if image_field:
                # Открываем изображение
                img = Image.open(image_field.path)

                # Устанавливаем фиксированные размеры
                target_width, target_height = 750, 500

                # Принудительно меняем размер изображения
                img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)

                # Сохраняем изменённое изображение
                img.save(image_field.path)

        # Масштабируем основное изображение
        resize_image(self.image)

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"

    def __str__(self):
        return self.name
    

class RareCar(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название машины")
    brand = models.CharField(max_length=20, null=True, blank=True, verbose_name="Брэнд")
    model = models.CharField(max_length=20, null=True, blank=True, verbose_name="Модель")
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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Сохраняем объект

        def resize_image(image_field):
            if image_field:
                # Открываем изображение
                img = Image.open(image_field.path)

                # Устанавливаем фиксированные размеры
                target_width, target_height = 750, 500

                # Принудительно меняем размер изображения
                img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)

                # Сохраняем изменённое изображение
                img.save(image_field.path)

        # Масштабируем основное изображение
        resize_image(self.image)

        # Масштабируем дополнительные изображения
        resize_image(self.additional_image_1)
        resize_image(self.additional_image_2)
        resize_image(self.additional_image_3)
        resize_image(self.additional_image_4)
        resize_image(self.additional_image_5)

    class Meta:
        verbose_name = "редкую машину"
        verbose_name_plural = "Редкие машины"

    def __str__(self):
        return self.name