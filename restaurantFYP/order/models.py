from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import datetime

# Create your models here.
from restaurant.models import Food

class Order (models.Model):
    order_id = models.AutoField(max_length=10, primary_key=True)
    ordered_food = models.ManyToManyField(Food, through='Order_State')
    table_id = models.ForeignKey(User, on_delete=models.CASCADE)
    billed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.order_id)

class Order_State(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, default='')
    STATE_IN_CHOICE = (
        ('uncooked', 'uncooked'),
        ('cooked', 'cooked'),
        ('cancelled', 'cancelled'),
    )
    state = models.CharField(max_length=10, choices=STATE_IN_CHOICE, default='uncooked')

class Cart(models.Model):
    cart_id = models.AutoField(max_length=10, primary_key=True)
    carted_food = models.ManyToManyField(Food, through='Cart_State')
    table_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cart_id)

class Cart_State(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, default='')
    connect = models.IntegerField(default=1, editable=False)

class Order_State_Inline(admin.TabularInline):
    model = Order_State
    extra = 1

class Cart_State_Inline(admin.TabularInline):
    model = Cart_State
    extra = 1

class Order_Admin(admin.ModelAdmin):
    inlines = (Order_State_Inline,)

class Cart_Admin(admin.ModelAdmin):
    inlines = (Cart_State_Inline,)
