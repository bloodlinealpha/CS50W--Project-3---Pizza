import os 


from orders.models import Topping

f = open("../csv2/toppings.txt", "r")

for t in f:
	t = Topping(name=t)
	t.save()