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
    # Examples:
    url(r'^$', restaurant.views.login, name='login'),
	url(r'^home$', restaurant.views.block_home, name='home'),
	url(r'^menu$', restaurant.views.block_menu, name='menu'),
	url(r'^orders$', restaurant.views.block_orders, name='orders'),
	url(r'^services$', restaurant.views.block_services, name='services'),
	url(r'^cart$', restaurant.views.block_cart, name='cart'),
	url(r'^items$', restaurant.views.block_items, name='items'),
	#url(r'^services$', restaurant.views.services, name='services'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
