from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title
"""
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100, default='John Doe')
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    status = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

class Grocery(models.Model):
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='grocery', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    imageurl = models.URLField()
    status = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name
   
class StockName(models.Model):
    name = models.CharField(max_length = 255)
    class Meta:
        verbose_name_plural = 'StocksName'

    def __str__(self):
        return self.name
"""
class TradeInfo(models.Model):
    name = models.CharField(max_length=255)
    Date = models.DateField(auto_now_add=True)
    Open = models.DecimalField(max_digits=10, decimal_places=6)
    High = models.DecimalField(max_digits=10, decimal_places=6)
    Low = models.DecimalField(max_digits=10, decimal_places=6)
    Close = models.DecimalField(max_digits=10, decimal_places=6)
    Volume = models.IntegerField()

# By adding this class the date will be ordered according to each stock's opening
    class Meta:
        ordering = ['Date']

    def __str__(self):
        return self.name