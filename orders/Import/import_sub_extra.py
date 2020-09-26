import os
import csv

from orders.models import SubExtra

f = open("../csv2/sub_extras.csv")
reader = csv.reader(f)

for st, pr in reader:
	t = SubExtra(extra=st, price=pr)
	t.save()