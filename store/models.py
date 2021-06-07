from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __UserType__(self):
		return self.user

def create_profile(sender,instance,created,**kwargs):
	if created:
		Customer.objects.create(user=instance)
post_save.connect(create_profile,sender=User)


class Product(models.Model):
	
	name = models.CharField(max_length=200,default="Null")
	company_name = models.CharField(max_length=200,help_text="Maruti,Hundai,etc",default="Null")
	price = models.FloatField(default=500.0)
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	image1 = models.ImageField(null=True, blank=True)
	image2 = models.ImageField(null=True, blank=True)
	des = models.CharField(max_length=200, help_text="color,condition,any problem in past,etc",default='Null')
	Km= models.CharField(max_length=200,default='Null')
	location = models.CharField(max_length=25,default='Null')
	Owners = models.CharField(max_length=10,default='Null')
	Year = models.CharField(max_length=4,default=00)
	car = models.CharField(max_length=20,default='Not')
	g = models.BooleanField(default=False,null=True, blank=True)
	totalprice=models.FloatField(default=0.0)
	number=models.IntegerField(default=0000000)
	customer= models.CharField(max_length=20,default="Null")
	car_number=models.CharField(max_length=4,default="xx90")
	parts = models.BooleanField(default=False,null=True, blank=True)

    
	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

	@property
	def image1URL(self):
		try:
			url = self.image1.url
		except:
			url = ''
		return url

	@property
	def image2URL(self):
		try:
			url = self.image2.url
		except:
			url = ''
		return url

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	total = models.IntegerField(null=True)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.product)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	orderitem = models.ForeignKey(OrderItem, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	phone = models.IntegerField(null=True)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.order)

class blog(models.Model):
	Title=models.CharField(max_length=30)
	date= models.DateTimeField(auto_now_add=True)
	des=models.CharField(max_length=1000)
	image = models.ImageField(null=True, blank=True)
	au = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
