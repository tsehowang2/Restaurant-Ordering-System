from django.contrib import admin

# Register your models here.
from restaurant.models import Category, Food, Table, Food_Admin, Category_Admin


admin.site.register(Category, Category_Admin)
admin.site.register(Food, Food_Admin)
admin.site.register(Table)
