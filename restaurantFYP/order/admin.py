from django.contrib import admin

# Register your models here.
from order.models import Order, Order_Admin, Temp

admin.site.register(Order, Order_Admin)
admin.site.register(Temp)