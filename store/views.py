from django.shortcuts import render,redirect 
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder
from django import forms
from django.http import HttpResponse
from .form import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_exempt



def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator



@csrf_exempt
def store(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = Product.objects.filter(car='Yes')
	count= Product.objects.filter(car='Yes').count()
	context = {'products':products, 'cartItems':cartItems,'count':count}
	if request.method=="POST":
		query= request.POST['query']
		form = Product.objects.filter(name__contains=query)
		if form.exists():
			context2 = {'form':form}
			return render(request, 'store/view.html', context2)
		else:
			messages.info(request, 'Sorry No Query Found')
			return render(request, 'store/store.html', context)
	else:
		return render(request, 'store/store.html', context)


def cart(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	transaction_id= str(transaction_id)
	print(type(transaction_id))
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
		order.total=total
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		phone=data['shipping']['phone'],

		)

	return JsonResponse('Payment submitted..', safe=False)

@csrf_exempt
def home(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('store')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'store/login.html', context)

def register(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + username)
			return redirect('login')
	context={'form':form}
	return render(request, 'store/register.html',context)
def logoutUser(request):
	logout(request)
	return redirect('login')

def view(request,pk):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	form = Product.objects.filter(id=pk)
	context = {'form':form, 'cartItems':cartItems}
	return render(request, 'store/view.html', context)


def low(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = Product.objects.filter(car="Yes").order_by('totalprice')
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/low.html', context)


def high(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = Product.objects.filter(car="Yes").order_by('-totalprice')
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/high.html', context)

def location(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = Product.objects.filter(car="Yes").order_by('location')
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/location.html', context)

def vp(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	context = {'cartItems':cartItems}
	if request.method=="POST":
		query= request.POST['query']
		return v(request,query);
	return render(request, 'store/viewparts.html',context)

def v(request,query):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = Product.objects.filter(company_name__contains=query,parts=True)
	print(products)

	context = {'products':products,'cartItems':cartItems}


	return render(request, 'store/parts.html',context)


def tb(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	blogs = blog.objects.all()
	context = {'blogs':blogs,'cartItems':cartItems}
	return render(request, 'store/totalblogs.html',context)

def viewblog(request,pk):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	blogs = blog.objects.filter(id=pk)
	
	context = {'blogs':blogs,'cartItems':cartItems}
	return render(request, 'store/blog.html',context)

def seller(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	context = {'cartItems':cartItems}
	return render(request, 'store/seller.html',context)


def sell(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	try:
		m = request.user.customer
	except:
		print('no user')
	form=ProductForm()

	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			
			form.save()
			messages.success(request, 'Request done successfully Please wait for verfication! ')

			return redirect('seller')
	context = {'cartItems':cartItems,'form':form}
	return render(request, 'store/sell.html',context)

@allowed_users(allowed_roles=['admin1'])	
def adminportal(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	context = {'cartItems':cartItems}
	return render(request, 'store/adminportal.html',context)



@allowed_users(allowed_roles=['admin1'])	
def createblogpage(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	form=CreateblogForm()
	if request.method == 'POST':
		form = CreateblogForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Post successfully! ')
			return redirect('adminportal')

	totalblog = blog.objects.all()
	context = {'cartItems':cartItems,'form':form,'totalblog':totalblog}
	return render(request, 'store/createblogpage.html',context)

@allowed_users(allowed_roles=['admin1'])	
def storedetails(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = Product.objects.filter(car='Yes')
	count= Product.objects.filter(car='Yes').count()
	products2 = Product.objects.filter(car='Not',parts=False)
	count2=Product.objects.filter(car='Not',parts=False).count()
	parts = Product.objects.filter(parts=True)
	print(parts)
	context = {'products':products, 'products2':products2,'cartItems':cartItems,'products':products,'count':count,'count2':count2,'parts':parts}
	return render(request, 'store/storedetails.html',context)

@allowed_users(allowed_roles=['admin1'])	
def view2(request,pk):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	form=Product.objects.filter(id=pk)
	context = {'form':form, 'cartItems':cartItems}
	
	if request.method=="POST":
		n = request.POST.get('r')
		if n == 'Yes':
			form.update(car='Yes')
		if n == "Not":
			form.update(car='Not')
		if n == "Delete":
			form.delete()
			return storedetails(request)
	return render(request, 'store/view2.html', context)

@allowed_users(allowed_roles=['admin1'])	
def viewblog2(request,pk):
	blogs = blog.objects.filter(id=pk).delete()
	messages.success(request, 'Deleted successfully! ')
	return render(request, 'store/adminportal.html')

@allowed_users(allowed_roles=['admin1'])	
def orders(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	count= ShippingAddress.objects.all().count()
	product=ShippingAddress.objects.all()
	context = {'cartItems':cartItems,'count':count,'product':product}
	
	return render(request, 'store/orders.html',context)

def ordersview(request,pk):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	t=Order.objects.get(transaction_id=pk)
	product=OrderItem.objects.filter(order=t)
	context = {'cartItems':cartItems,'product':product}
	return render(request, 'store/orderdetails.html',context)

def delete(request,pk):
	order = ShippingAddress.objects.filter(id=pk).delete()
	return orders(request)
