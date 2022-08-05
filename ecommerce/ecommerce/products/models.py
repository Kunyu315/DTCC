from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title


class TradeInfo(models.Model):
    Name = models.CharField(max_length=255)
    Date = models.DateField(auto_now_add=False)
    Open = models.DecimalField(max_digits=10, decimal_places=6)
    High = models.DecimalField(max_digits=10, decimal_places=6)
    Low = models.DecimalField(max_digits=10, decimal_places=6)
    Close = models.DecimalField(max_digits=10, decimal_places=6)
    Volume = models.IntegerField()

# By adding this class the date will be ordered according to each stock's opening
    class Meta:
        ordering = ['Date']

    def __str__(self):
        return self.Name