from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from restaurant.models import Category, Food, Table
from order.models import Order
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):

    return render(
        request,
        'restaurant/index.html',
    )


def login(request):
    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            return redirect('login')
    else:
        return render(request, 'restaurant/login.html',)

@login_required(redirect_field_name='login')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('login')

@login_required(redirect_field_name='login')
def block_home(request):
	"""Renders the home page."""
	return render(
        request,
        'restaurant/block_home.html',
    )

@login_required(redirect_field_name='login')
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

@login_required(redirect_field_name='login')
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

@login_required(redirect_field_name='login')
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

@login_required(redirect_field_name='login')
def block_orders(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    return render(
        request,
        'restaurant/block_orders.html',
        {
            
        }
    )

@login_required(redirect_field_name='login')
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

@login_required(redirect_field_name='login')
def block_services(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    return render(
        request,
        'restaurant/block_services.html',
        {
            
        }
    )

@login_required(redirect_field_name='login')
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

@login_required(redirect_field_name='login')
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

@login_required(redirect_field_name='login')
def cart(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    return render(
        request,
        'restaurant/cart.html',
        {
            
        }
    )

@login_required(redirect_field_name='login')
def block_items(request):
	"""Renders the home page."""
	#assert isinstance(request, HttpRequest)
	query = request.GET.get('name')
	print(query)
	foods = Food.objects.filter(category_id = query)
	print(foods)
	title = Category.objects.filter(category_id = query)
	args = {'Food': foods, 'Title': title}
	return render(
		request,
		'restaurant/block_items.html',
		args,
    )

@login_required(redirect_field_name='login')
def items(request):
	"""Renders the home page."""
	#assert isinstance(request, HttpRequest)
	return render(
        request,
        'restaurant/items.html',
    )