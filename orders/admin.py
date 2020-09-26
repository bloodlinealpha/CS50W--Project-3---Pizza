from django.contrib import admin
from .models import Menu, Pizza, Topping, Sub, SubExtra, Platter, Cart, Order, PizzaOrder

# Register your models here.
admin.site.register(Menu)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(SubExtra)
admin.site.register(Platter)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(PizzaOrder)
