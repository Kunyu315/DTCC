from django.contrib import admin
from .models import Category, TradeInfo

from import_export.admin import ImportExportModelAdmin

from products import models
"""
# Register your models here.
admin.site.register(Category)
#admin.site.register(Book)
admin.site.register(TradeInfo)
"""

@admin.register(models.TradeInfo)
class TradeInfoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    # your admin logic for the model

    #admin.site.register(TradeInfo)
    ...
    
