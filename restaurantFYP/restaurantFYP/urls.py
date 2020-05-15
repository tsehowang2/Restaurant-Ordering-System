"""
Definition of urls for restaurantFYP.
"""

from datetime import datetime
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
import django.contrib.auth.views

import app.forms
import app.views

import restaurant.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', restaurant.views.index, name='index'),
    url(r'^login$', restaurant.views.login, name='login'),
    url(r'^logout$', restaurant.views.logout, name='logout'),
    url(r'^thankyou$', restaurant.views.thankyou, name='thankyou'),
	url(r'^home$', restaurant.views.block_home, name='home'),
	url(r'^home/menu$', restaurant.views.block_menu, name='menu'),
	url(r'^orders$', restaurant.views.block_orders, name='orders'),
	url(r'^services$', restaurant.views.block_services, name='services'),
	url(r'^cart$', restaurant.views.block_cart, name='cart'),
    url(r'^bill$', restaurant.views.bill_page, name='bill'),
	url(r'^home/menu/items$', restaurant.views.block_items, name='items'),
    url(r'^home/menu/addtocart$', restaurant.views.add_to_cart, name='add_to_cart'),
    url(r'^removefromcart$', restaurant.views.remove_from_cart, name='remove_from_cart'),
    url(r'^proceedorder$', restaurant.views.proceed_order, name='proceed_order'),
    url(r'^returnorder$', restaurant.views.return_order, name='return_order'),
    url(r'^getorderstate$', restaurant.views.get_order_state, name='get_order_state'),
    url(r'^billed$', restaurant.views.billed, name='billed'),
    url(r'^services/add_water$', restaurant.views.service_add_water, name='service_add_water'),
    url(r'^services/clean_table$', restaurant.views.service_clean_table, name='service_clean_table'),
    url(r'^services/baby_chair$', restaurant.views.service_baby_chair, name='service_baby_chair'),
    url(r'^force_logout$', restaurant.views.force_logout, name='force_logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls, name='admin'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#haha