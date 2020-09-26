import os
import csv

from orders.models import Pizza

f = open("../csv2/pizza.csv")
reader = csv.reader(f)

for st, top, si, pr in reader:
	t = Pizza(style=st, size=si, topping=top, price=pr)
	t.save()