from django.contrib import admin

# Register your models here.
from restaurant.models import Category, Food, Table
from order.models import Food_Admin


admin.site.register(Category)
admin.site.register(Food, Food_Admin)
admin.site.register(Table)
