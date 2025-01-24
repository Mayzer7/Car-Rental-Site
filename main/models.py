from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя сотрудника")
    post = models.CharField(max_length=20, verbose_name="Должность")
    image = models.ImageField(upload_to='person/', verbose_name="Фото сотрудника")

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return self.name