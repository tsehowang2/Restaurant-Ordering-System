from django.contrib import admin

# Register your models here.
from order.models import Order, Order_Admin, Cart, Cart_Admin

admin.site.register(Order, Order_Admin)
admin.site.register(Cart, Cart_Admin)