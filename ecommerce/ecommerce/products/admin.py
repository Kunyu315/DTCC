from django.contrib import admin
from .models import Category, TradeInfo

# Register your models here.
admin.site.register(Category)
#admin.site.register(Book)
admin.site.register(TradeInfo)