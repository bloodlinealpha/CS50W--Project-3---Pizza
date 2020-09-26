import os
import csv

from orders.models import Sub

f = open("../csv2/subs.csv")
reader = csv.reader(f)

for st, si, pr in reader:
	t = Sub(name=st, size=si, price=pr)
	t.save()