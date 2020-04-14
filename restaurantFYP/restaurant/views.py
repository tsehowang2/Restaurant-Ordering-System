from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from restaurant.models import Category, Food
from order.models import Order, Order_State, Cart, Cart_State
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime

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
    hasOrder = False
    try:
       bill = Order.objects.get(table_id = auth.get_user(request), billed = False)
       hasOrder = True
    except Order.DoesNotExist:
        hasOrder = False
    print(hasOrder)
    args = {'hasOrder': hasOrder}
    print(args)
    return render(
        request,
        'restaurant/block_home.html',
        args,
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
    bill = Order.objects.get(table_id = auth.get_user(request), billed = False),
    foodlist = []
    for table in bill:
        state = Order_State.objects.filter(order = table)
        for state in state:
            foodlist.append(state)
    context = {'foodlist' : foodlist}
    return render(
        request,
        'restaurant/block_orders.html',
        context
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
    cart = Cart.objects.filter(table_id = auth.get_user(request))
    foodlist = []
    for cart in cart:
        cart_food = cart.carted_food.all()
        for food in cart_food:
            foodlist.append(food)
    context = {'cart': foodlist}
    template = 'restaurant/block_cart.html'
    return render(request, template, context)

@login_required(redirect_field_name='login')
def cart(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    return render(
        request,
        'restaurant/cart.html',
    )

@login_required(redirect_field_name='login')
def block_items(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    query = request.POST.get('name')
    foods = Food.objects.filter(category_id = query)
    foods = Food.objects.filter(available = True)
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

@login_required(redirect_field_name='login')
def add_to_cart(request):
   food_id = request.POST.get('food_id')
   quantity = int(request.POST.get('quantity'))
   print(food_id)
   print(quantity)
   food = Food.objects.get(food_id=food_id)
   try:
        cart = Cart.objects.get(table_id=auth.get_user(request))
   except Cart.DoesNotExist:
        cart = Cart.objects.create(table_id=auth.get_user(request))
   for x in range(quantity):
        cart_state = Cart_State.objects.create(cart=cart, food=food)

   return HttpResponse('')

@login_required(redirect_field_name='login')
def remove_from_cart(request):
   food_id = request.POST.get('food_id')
   food = Food.objects.get(food_id=food_id)
   cart = Cart.objects.get(table_id=auth.get_user(request))
   cart_state = Cart_State.objects.filter(cart=cart, food=food).first()
   cart_state.delete()
   return HttpResponse('')