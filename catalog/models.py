from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator

from src.constants import NULLABLE
from users.models import User


# Описание модели Продуктов
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    image = models.ImageField(upload_to='products', **NULLABLE, verbose_name='изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена за покупку')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')
    # Поле для хранения пользователя, который создал продукт
    owner = models.ForeignKey(User, on_delete=models.PROTECT, **NULLABLE)

    # def save(self, *args, **kwargs):
    #     if self.pk is None:  # Проверка, что модель создается (а не обновляется)
    #         self.owner = kwargs.pop('request').user  # Получаем пользователя из запроса
    #
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    # Метаданные для обозначения модели
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


# Описание модели Категорий
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')

    def __str__(self):
        return self.name

    # Метаданные для обозначения модели
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Описание модели Версий
class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name='Номер версии')
    name = models.CharField(max_length=100, verbose_name='Имя версии')
    is_active = models.BooleanField(default=False, verbose_name='Признак текущей версии')

    def __str__(self):
        return f"{self.product.name} - Версия {self.number}"

    # Метаданные для обозначения модели
    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
