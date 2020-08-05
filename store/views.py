from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from .models import *
import json
import datetime

from .utils import cart_data
# Create your views here.


def home(request):
    products = Product.objects.all()

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items

    else:
        data = cart_data(request)
        cart_items = data['cart_items']
    context = {
        'products': products,
        'cart_items': cart_items,
    }
    return render(request, 'store/index.html', context)


def cart(request):
    data = cart_data(request)

    context = {
        'items': data['items'],
        'order': data['order'],
        'cart_items': data['cart_items'],
    }

    return render(request, 'store/cart.html', context)


def checkout(request):
    data = cart_data(request)

    context = {
        'items': data['items'],
        'order': data['order'],
        'cart_items': data['cart_items'],
    }

    return render(request, 'store/checkout.html', context)


def update_cart(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    # print(productId, action)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    order_item, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        order_item.quantity = order_item.quantity + 1
    elif action == 'remove':
        order_item.quantity = order_item.quantity - 1
    elif action == 'remove_item':
        order_item.quantity = 0

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse("Item was added", safe=False)


def process_order(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    customer = request.user.customer
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    total = data['form']['total']
    order.transaction_id = transaction_id

    if float(total) == float(order.get_cart_total):
        order.complete = True
        order.save()
        Shipping.objects.create(customer=request.user.customer, order=order,
                            address=data['shipping']['address'], city=data['shipping']['city'], state=data['shipping']['state'], zipcode=data['shipping']['zipcode'])

    return JsonResponse("Order processed", safe=False)


def sign_up(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')

    print(first_name, last_name, email, password1, password2)
    return render(request, 'store/sign_up.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            msg = "Invalid username or password!"
            return render(request, 'store/login.html', {'msg': msg})
    return render(request, 'store/login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
# def contact(request):
#     context = {}
#     return render(request, 'store/contact.html', context)


# def about(request):
#     context = {}
#     return render(request, 'store/about.html', context)
