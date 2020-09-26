from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Menu(models.Model):
	item = models.CharField(max_length=64)

	def __str__(self):
  		return f"id:{self.id} - {self.item}"

class Pizza(models.Model):
	style = models.CharField(max_length=64)
	size = models.CharField(max_length=64)
	topping = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
  		return f"id:{self.id} - {self.style}- {self.size}- {self.topping}- {self.price}"

class Topping(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
  		return f"id:{self.id} - {self.name}"

class Sub(models.Model):
	name = models.CharField(max_length=64)
	size = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
  		return f"id:{self.id} - {self.name} - {self.size} - {self.price}"	

class SubExtra(models.Model):
	extra = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=5, decimal_places=2)


	def __str__(self):
		return f"id:{self.id} - {self.extra} - {self.price}"

class Platter(models.Model):
	name = models.CharField(max_length=64)
	size = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
  		return f"id:{self.id} - {self.name} - {self.size} - {self.price}"

class PizzaOrder(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	style = models.CharField(max_length=64)
	size = models.CharField(max_length=64)
	toppings = models.CharField(max_length=64)
	topping_1 = models.CharField(max_length=64)
	topping_2 = models.CharField(max_length=64)
	topping_3 = models.CharField(max_length=64)
	extra_1 = models.CharField(max_length=64, default="")
	extra_2 = models.CharField(max_length=64, default="")
	extra_3 = models.CharField(max_length=64, default="")
	extra_4 = models.CharField(max_length=64, default="")
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
  		return f"id:{self.id} - {self.user}- {self.style}- {self.size}- {self.toppings}- {self.topping_1}- {self.topping_2}- {self.topping_3}-- {self.extra_1}- {self.extra_2}- {self.extra_3}- {self.extra_4}- {self.price}"


class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	create_time = models.DateTimeField(auto_now_add=True)
	pizza_order = models.ForeignKey(PizzaOrder, on_delete=models.CASCADE, related_name="cart_order")
	ordered = models.BooleanField(default=False)
	
	def __str__(self):
  		return f"id:{self.id} {self.create_time} - {self.pizza_order}"

class Order(models.Model):
	STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Complete', 'Complete'),
    
]

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	status = models.CharField(max_length=32,choices=STATUS_CHOICES, default="PENDING")
	create_time = models.DateTimeField(auto_now_add=True)
	items = models.ForeignKey(Cart, on_delete=models.CASCADE)
	


	def __str__(self):
  		return f"id:{self.id} - {self.user} - {self.status}- {self.create_time}- {self.items}"

