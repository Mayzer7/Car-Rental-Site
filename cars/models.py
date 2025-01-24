from PIL import Image
from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название машины")
    brand = models.CharField(max_length=20, null=True, blank=True, verbose_name="Брэнд")
    # model = models.CharField(max_length=20, null=True, blank=True, verbose_name="Модель")
    mileage = models.PositiveIntegerField(verbose_name="Пробег (в км)")
    year = models.PositiveIntegerField(verbose_name="Год выпуска")
    transmission = models.CharField(max_length=50, verbose_name="Привод", choices=(
        ('manual', 'Manual'),
        ('automatic', 'Automatic')
    ))
    location = models.CharField(max_length=255, verbose_name="Адрес")
    car_type = models.CharField(max_length=50, verbose_name="Тип машины", choices=(
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('truck', 'Truck'),
        ('coupe', 'Coupe')
    ))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена аренды")
    image = models.ImageField(upload_to='cars/', verbose_name="Изображение (750x500px)")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Сохраняем объект
        if self.image:
            # Открываем изображение
            img = Image.open(self.image.path)

            # Устанавливаем фиксированные размеры
            target_width, target_height = 750, 500

            # Принудительно меняем размер изображения
            img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)

            # Сохраняем изменённое изображение
            img.save(self.image.path)

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"

    def __str__(self):
        return self.name