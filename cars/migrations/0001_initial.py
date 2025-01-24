# Generated by Django 5.1.4 on 2025-01-21 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название машины')),
                ('mileage', models.PositiveIntegerField(verbose_name='Пробег (в км)')),
                ('year', models.PositiveIntegerField(verbose_name='Год выпуска')),
                ('transmission', models.CharField(choices=[('manual', 'Manual'), ('automatic', 'Automatic')], max_length=50, verbose_name='Привод')),
                ('location', models.CharField(max_length=255, verbose_name='Адрес')),
                ('car_type', models.CharField(choices=[('sedan', 'Sedan'), ('suv', 'SUV'), ('truck', 'Truck'), ('coupe', 'Coupe')], max_length=50, verbose_name='Тип машины')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена аренды')),
                ('image', models.ImageField(upload_to='cars/', verbose_name='Основное изображение')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
            },
        ),
    ]
