from django.db import models
from django.contrib import admin

# Create your models here.
from restaurant.models import Food, Table




class Order (models.Model):
    order_id = models.AutoField(max_length=10, primary_key=True)
    
    ordered_food = models.ManyToManyField(Food, through='Order_State')
    table_id = models.ForeignKey(Table)
    billed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.order_id)


class Order_State(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, default='')
    quantity = models.IntegerField(default=1)
    STATE_IN_CHOICE = (
        ('uncooked', 'uncooked'),
        ('cooked', 'cooked'),
        ('cancelled', 'cancelled'),
    )
    state = models.CharField(max_length=10, choices=STATE_IN_CHOICE, default='uncooked')

class Order_State_Inline(admin.TabularInline):
    model = Order_State
    extra = 1


class Order_Admin(admin.ModelAdmin):
    inlines = (Order_State_Inline,)


