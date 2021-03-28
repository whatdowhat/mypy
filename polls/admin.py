from django.contrib import admin
from . import models
# from .models import StockComeR
# Register your models here.

class StockComeR(admin.ModelAdmin):
    list_display = (
         'key',
        'nm_kr',
        'nm_en'
    )
    
admin.site.register(models.StockComeR,StockComeR)
