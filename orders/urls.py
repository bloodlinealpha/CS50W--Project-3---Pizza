from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("platters", views.platter, name="platter"),
	path("cart", views.cart, name="cart"),
	path("order", views.adminOrder, name="order"),
	

]