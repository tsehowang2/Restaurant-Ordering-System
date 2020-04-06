from django.contrib import admin

# Register your models here.
from restaurant.models import Category, Food, Category_Admin, Food_Admin


admin.site.register(Category, Category_Admin)
admin.site.register(Food, Food_Admin)