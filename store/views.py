from django.shortcuts import render, redirect
from .models import Product, Order, OrderItem, ShippingAdress
from django.contrib.auth.models import User
from django.http import JsonResponse
from .forms import UserRegistrationForm
from django.contrib import messages
import json
import time
import datetime
from .utils import *
from django.contrib.auth.decorators import login_required, permission_required


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            ak = form.save()
            # ak return user name
            user = form.cleaned_data.get('user')
            messages.success(
                request, f" Your account has been {user} sucesfully created please register")
            return redirect('login')

    else:
        form = UserRegistrationForm()

    return render(request, 'store/register.html', {"form": form})


def get_total(user):
    if user.is_authenticated:
        customer = user.username
        order, created = Order.objects.get_or_create(
            customer_id=user.id, complete=False)
        items = order.orderitem_set.all()
        context = {'items': items, 'orders': order, }
    return context


def store(request):

    products = Product.objects.all()

    if request.user.is_authenticated:
        context = {'products': products, 'orders': get_total(request.user)[
            'orders']}
    else:
        items = {'totalPrice': 0}
        order = {'totalPrice': 0, 'totalItem': 0}
        context = {'products': products, 'items': items,
                   'orders': order, 'shipping': False}
    return render(request, 'store/Store.html', context)


def cardView(request, prod_id):
    if request.user.is_authenticated:
        context = get_total(request.user)

    else:
        context = {}

    product = Product.objects.get(id=prod_id)

    context['product'] = product
    return render(request, 'store/viewItem.html', context)


def card(request):

    if request.user.is_authenticated:
        context = get_total(request.user)

    else:
        context = nonuser(request)
    return render(request, 'store/Card.html', context)


def checkout(request):
    if request.user.is_authenticated:
        context = get_total(request.user)
        last_shipping_address = ShippingAdress(request.user)

    else:
        context = nonuser(request)
    return render(request, 'store/Checkout.html', context)


def updateItem(request):
    body = json.loads(request.body)
    productId = body['productId']
    action = body['action']
    customer = request.user.username
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer_id=request.user.id, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(
        product=product, order=order)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity+1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity-1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('card has been added up safely', safe=False)


def processOrder(request):
    data = json.loads(request.body)
    transaction_id = datetime.datetime.now().timestamp()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        order.transaction_id = transaction_id
        if "{:.2f}".format(float(data['userFormInfo']['total'])) == "{:.2f}".format(float(order.totalPrice)):
            order.complete = True

        if order.shipping:
            ShippingAdress.objects.create(
                address=data['shippingFormData']['adress'], customer=customer, order=order, country=data['shippingFormData']['country'],
                state=data['shippingFormData']['state'], city=data['shippingFormData']['city'],  zipcode=data['shippingFormData']['zipcode'])
        order.save()
    else:
        print("user  has not logged in !")

    print(request.body)
    return JsonResponse('Process is completed', safe=False)
