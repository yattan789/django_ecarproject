from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('login/', views.home, name="login"),
	path('register/', views.register, name="register"),
    path('logout/', views.logoutUser, name='logout'),
    path('view/<int:pk>', views.view, name="view"),
	path('low', views.low, name="low"),
	path('high', views.high, name="high"),
	path('location', views.location, name="location"),
	path('vp', views.vp, name="vp"),
	path('v', views.v, name="v"),
	path('tb', views.tb, name="tb"),
    path('viewblog/<int:pk>', views.viewblog, name="viewblog"),
    path('seller', views.seller, name="seller"),  
    path('sell', views.sell, name="sell"),   
    path('adminportal', views.adminportal, name="adminportal"),   
    path('createblogpage', views.createblogpage, name="createblogpage"),   
    path('storedetails', views.storedetails, name="storedetails"),   
    path('view2/<int:pk>', views.view2, name="view2"), 
    path('viewblog2/<int:pk>', views.viewblog2, name="viewblog2"),
	path('orders', views.orders, name="orders"),
	path('ordersview/<str:pk>', views.ordersview, name="ordersview"),
	path('delete/<int:pk>', views.delete, name="delete"),
]