from django.db import models
from django.contrib import admin

# Create your models here.

class Category(models.Model):
    category_id = models.AutoField(max_length=10, primary_key=True)
    category_name = models.CharField(unique=True, max_length=20)
    image = models.ImageField(upload_to='menu/category')
    
    def __str__(self):
        return str(self.category_name)

class Food(models.Model):
    food_id = models.CharField(max_length=10, primary_key=True)
    food_name = models.CharField(max_length=50)
    category_id = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='menu/food')
    available = models.BooleanField(default=True)

    def __str__(self):
        return '{} {} {} {}'.format(self.food_id, self.food_name, self.price, self.available)

class Table(models.Model):
    table_id = models.CharField(max_length=10, primary_key=True)
    avab_to_cust = models.BooleanField(default=True)

    def __str__(self):
        return str(self.table_id)

class Food_Admin(admin.ModelAdmin):
	list_display = ('food_id', 'food_name', 'price', 'available')

class Category_Admin(admin.ModelAdmin):
	list_display = ('category_id', 'category_name')
