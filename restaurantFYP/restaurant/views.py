from django.shortcuts import render

from django.http import HttpRequest
from django.template import RequestContext
from restaurant.models import Category, Food, Table
from order.models import Order
from django.views.generic import TemplateView

# Create your views here.
def block_home(request):
	"""Renders the home page."""
	return render(
        request,
        'restaurant/block_home.html',
        {
            
        }
    )
def home(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    return render(
        request,
        'restaurant/home.html',
        {
            'title':'Home Page',
			'header':'Welcome',
        }
    )
def block_menu(request):
	"""Renders the home page."""
	#assert isinstance(request, HttpRequest)
	category = Category.objects.exclude(category_name = 'Drinks')
	category = category.exclude(category_name =  'Snacks')
	drinks = Category.objects.filter(category_name = 'Drinks')
	snacks = Category.objects.filter(category_name = 'Snacks')
	args = {'Category': category, 'Drinks': drinks, 'Snacks': snacks}
	return render(
        request,
        'restaurant/block_menu.html',
		args,
    )
def menu(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    return render(
        request,
        'restaurant/menu.html',
        {
            'title':'Menu',
        }
    )
def block_orders(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    return render(
        request,
        'restaurant/block_orders.html',
        {
            
        }
    )
def orders(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    return render(
        request,
        'restaurant/orders.html',
        {
            'title':'Orders',
        }
    )
def block_services(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    return render(
        request,
        'restaurant/block_services.html',
        {
            
        }
    )
def services(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    return render(
        request,
        'restaurant/services.html',
        {
            'title':'Services',
        }
    )
def block_cart(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    return render(
        request,
        'restaurant/block_cart.html',
        {
            'value':'Default',
        }
    )
def cart(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    return render(
        request,
        'restaurant/cart.html',
        {
            
        }
    )
def block_items(request):
	"""Renders the home page."""
	#assert isinstance(request, HttpRequest)
	return render(
		request,
		'restaurant/block_items.html',
    )
def items(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)

    return render(
        request,
        'restaurant/items.html',
        {
            
        }
    )