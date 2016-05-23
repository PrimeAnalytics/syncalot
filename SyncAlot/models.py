from django.db import models
from django.utils.datetime_safe import datetime


class User(models.Model):
    email = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)


class Product(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    product_code = models.CharField(max_length=30, primary_key=True)
    category = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)


class ProductUrl(models.Model):
    product_code = models.ForeignKey(Product, on_delete=models.CASCADE)
    url = models.CharField(max_length=255, primary_key=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    stock = models.IntegerField(default=0)
    description = models.TextField(default='')
    name = models.CharField(max_length=255, default='')
    last_check = models.DateTimeField(blank=True, default=datetime.now)


class Scraper(models.Model):
    import_io_extractor_id = models.CharField(max_length=255, default='')
    import_io_api_key = models.CharField(max_length=255, default='')
    host = models.CharField(max_length=255, primary_key=True)
