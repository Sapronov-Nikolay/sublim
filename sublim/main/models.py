from django.db import models
from datetime import datetime


class Category(models.Model):
    categoriya = models.CharField(max_length=50, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=False, null=False, verbose_name='URL')

    class Meta:
        verbose_name = 'Категорию'  # Единственное число
        verbose_name_plural = 'Категории'  # Множественное число

    def __str__(self):
        return self.categoriya  # Отображает имя, вместо "Category object(pk) pk - это ID"


class Good(models.Model):
    picture = models.ImageField(default=0, upload_to="images/%y/%m/%d/", verbose_name='Фото')
    namegood = models.CharField(max_length=30, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Описание')
    specification = models.CharField(max_length=300, verbose_name='Спецификация')
    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0, max_digits=2, decimal_places=0, verbose_name='Скидка в %')
    quatity = models.PositiveIntegerField(default=0, verbose_name='Количество в уп')
    quatity2 = models.FloatField(default=0.00, verbose_name='Вес в кг')
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, null=True, verbose_name='Категория')

    class Meta:
        verbose_name = 'Товар'  # Единственное число
        verbose_name_plural = 'Товары'  # Множественное число

    def __str__(self):
        return self.namegood  # Отображает имя, вместо "Good object(pk) pk - это ID"



# ------------------СТОИТ СДЕЛАТЬ В ОТДЕЛЬНОМ ПРИЛОЖЕНИИ------------------------------------
# ДАННУЮ МОДЕЛЬ СЛЕДУЕТ ПЕРЕДЕЛАТЬ, ТАК КАК В АДМИНКЕ ОНА ОТОБРАЖАЕТСЯ КАК ТОВАР
            # И МОЖНО СОЗДАТЬ МНОГО КОРЗИНОК
class Cart(models.Model):
    picture = models.ImageField(default=0, upload_to="images/%y/%m/%d/", verbose_name='Изображиние')
    namegood = models.CharField(max_length=30, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    price = models.FloatField(verbose_name='Название')

    class Meta:
        verbose_name = 'Корзину'  # Единственное число ДОБАВИТЬ В
        verbose_name_plural = 'Корзина'  # Единственное число ОДНА КОРЗИНА

    def __str__(self):
        return str(self.namegood)  # Отображает имя, вместо "Cart object(pk) pk - это ID"