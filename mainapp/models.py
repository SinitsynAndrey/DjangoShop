from django.db import models


class Products_categories(models.Model):
    name = models.CharField(verbose_name='название', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(Products_categories, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название', max_length=128)
    image = models.ImageField(upload_to='products', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание', max_length=128, blank=True)
    description = models.TextField(verbose_name='описание', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='колличество товара', default=0)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name
