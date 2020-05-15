from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import datetime

# Create your models here.
from restaurant.models import Food

class Order (models.Model):
    order_id = models.AutoField(primary_key=True)
    ordered_food = models.ManyToManyField(Food, through='Order_State', blank=True, default=None)
    table_id = models.ForeignKey(User, on_delete=models.CASCADE)
    billed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.order_id)

    def ordered(self):
        return ",".join([food.food_name for food in self.ordered_food.all()])

    def total_price(self):
        order = Order_State.objects.filter(order=self).exclude(state='cancelled')
        total_price = 0
        for order in order:
            total_price += order.food.price
        return total_price

    def is_billed(self):
        if self.billed == True:
            return True
        return False

class Order_State(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True)
    STATE_IN_CHOICE = (
        ('ordered', 'ordered'),
        ('making', 'making'),
        ('finished', 'finished'),
        ('served', 'served'),
        ('cancelled', 'cancelled'),
    )
    state = models.CharField(max_length=10, choices=STATE_IN_CHOICE, default='ordered')

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    carted_food = models.ManyToManyField(Food, through='Cart_State')
    table_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cart_id)

    def carted(self):
        return ",".join([food.food_name for food in self.carted_food.all()])

class Cart_State(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, default='')
    connect = models.IntegerField(default=1, editable=False)

class Order_State_Inline(admin.TabularInline):
    model = Order_State
    extra = 0
    
class Cart_State_Inline(admin.TabularInline):
    model = Cart_State
    extra = 0

class Order_Admin(admin.ModelAdmin):
    inlines = (Order_State_Inline,)
    list_display = ('table_id', 'ordered', 'total_price', 'is_billed')
    list_filter = ('billed',)
    ordering = ('billed', 'table_id',)

class Cart_Admin(admin.ModelAdmin):
    inlines = (Cart_State_Inline,)
    list_display = ('table_id', 'carted',)
    ordering = ('table_id',)
