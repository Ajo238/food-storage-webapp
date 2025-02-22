from django.contrib import admin

from .models import FoodItem

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'unit', 'expiry_date', 'added_on', 'is_expired')
    search_fields = ('name', 'category')
    list_filter = ('category', 'expiry_date')
   # admin.site.register(FoodItem)

