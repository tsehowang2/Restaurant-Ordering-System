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
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
import itertools
import json

# Create your views here.
def index(request):

    return render(
        request,
        'restaurant/index.html',
    )


def login(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return HttpResponse('<h1>Please scan QR code in order to use our website</h1>')

    #elif request.method == 'POST': 
    #    username = request.POST.get('username')
    #    password = request.POST.get('password')
    #
    #    user = auth.authenticate(username=username, password=password)
    #
    #    if user is not None:
    #        auth.login(request, user)
    #        return redirect("home")
    #    else:
    #        return redirect('login')
    else:
        return HttpResponse('Please scan QR code in order to use our website')

@login_required(redirect_field_name='login')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('login')

@login_required(redirect_field_name='login')
def block_home(request):
    """Renders the home page."""
    hasOrder = False
    total = 0
    try:
       bill = Order.objects.get(table_id = auth.get_user(request), billed = False)
       hasOrder = True
       state = Order_State.objects.filter(order = bill)
       for state in state:
           if state.state != 'cancelled':
               total += state.food.price
    except Order.DoesNotExist:
        hasOrder = False
    args = {'hasOrder': hasOrder, 'total': total}
    #print(args)
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
def billed(request):
    try:
        bill = Order.objects.get(table_id = auth.get_user(request), billed = False)
        bill.billed = True
        bill.save()
    except Order.DoesNotExist:
        pass
    try:
        cart = Cart.objects.filter(table_id = auth.get_user(request))
        cart.delete()
    except Cart.DoesNotExist:
        pass
    auth.logout(request)
    return HttpResponseRedirect('login')

@login_required(redirect_field_name='login')
def block_menu(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    category = Category.objects.exclude(category_name = 'Drinks')
    category = category.exclude(category_name =  'Snacks')
    drinks = Category.objects.filter(category_name = 'Drinks')
    snacks = Category.objects.filter(category_name = 'Snacks')
    cart = Cart.objects.filter(table_id = auth.get_user(request))
    total = 0
    for cart in cart:
        cart_food = cart.carted_food.all()
        for food in cart_food:
            total += food.price
    args = {'Category': category, 'Drinks': drinks, 'Snacks': snacks, 'Total': total}
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
    bill = Order.objects.get(table_id = auth.get_user(request), billed = False)
    foodlist = []
    total = 0
    state = Order_State.objects.filter(order = bill)
    #print(state)
    #print(state[0].state)
    for state in state:
        foodlist.append(state)
        if state.state != 'cancelled':
            total += state.food.price
    context = {'foodlist' : foodlist, 'total': total}
    return render(
        request,
        'restaurant/block_orders.html',
        context,
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
    category_id = request.POST.get('category_id')
    cart = Cart.objects.filter(table_id = auth.get_user(request))
    foodlist = []
    for cart in cart:
        cart_food = cart.carted_food.all()
        for food in cart_food:
            foodlist.append(food)
    context = {'cart': foodlist, 'category_id': category_id}
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
    category_id = request.POST.get('category_id')
    print(category_id)
    foods = Food.objects.filter(category_id = category_id, available = True)
    title = Category.objects.filter(category_id = category_id)
    cart = Cart.objects.filter(table_id = auth.get_user(request))
    total = 0
    for cart in cart:
        cart_food = cart.carted_food.all()
        for food in cart_food:
            total += food.price
    args = {'Food': foods, 'Title': title, 'category_id': category_id, 'Total': total}
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
    #print(food_id)
    #print(quantity)
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

@login_required(redirect_field_name='login')
def proceed_order(request):
    table_id = auth.get_user(request)
    cart = Cart.objects.filter(table_id = table_id)
    for cart in cart:
        cart_food = cart.carted_food.all()
        for food in cart_food:
            try:
                order = Order.objects.get(table_id = auth.get_user(request), billed = False)
            except Order.DoesNotExist:
                order = Order.objects.create(table_id=auth.get_user(request))
            #print(order)
            order_state = Order_State.objects.create(order=order, food=food, state='ordered')
    cart.delete()
    #"""Renders the home page."""
    proceed_order = True
    hasOrder = False
    total = 0
    try:
       bill = Order.objects.get(table_id = auth.get_user(request), billed = False)
       hasOrder = True
       state = Order_State.objects.filter(order = bill)
       for state in state:
           if state.state != 'cancelled':
               total += state.food.price
    except Order.DoesNotExist:
        hasOrder = False
    args = {'hasOrder': hasOrder, 'total': total, 'proceed_order': proceed_order}
    #print(args)
    return render(
        request,
        'restaurant/block_home.html',
        args,
    )

@login_required(redirect_field_name='login')
def return_order(request):
    index = int(request.POST.get('index'))
    bill = Order.objects.get(table_id = auth.get_user(request), billed = False)
    tryLoop = Order_State.objects.filter(order = bill)
    counter = 0;
    for stuff in tryLoop:
        #print("targeted index: ", index, " | ", counter, " :current")
        #print(stuff)
        if counter == index:
            if stuff.state == 'ordered' or stuff.state == 'making':
                stuff.state = 'cancelled'
                stuff.save()
            break
        else:
            counter = counter + 1
    return HttpResponse('')

@login_required(redirect_field_name='login')
def get_order_state(request):
    bill = Order.objects.filter(table_id = auth.get_user(request), billed = False)
    lists = Order_State.objects.filter(order = bill).only('state')
    result = []
    for state in lists:
        result.append(state.state)
    return JsonResponse(result, safe=False)