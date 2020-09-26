from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render

from .models import Pizza, Topping, Sub, SubExtra, Platter, Cart, Order, PizzaOrder




# Create your views here.
def index(request):

	table_1 = Pizza.objects.filter(style__iexact= "Regular Pizza", size__iexact= "Small")
	table_2 = Pizza.objects.filter(style__iexact= "Regular Pizza", size__iexact= "large")
	table_3 = Pizza.objects.filter(style__iexact= "Sicilian Pizza", size__iexact= "Small")
	table_4 = Pizza.objects.filter(style__iexact= "Sicilian Pizza", size__iexact= "large")

	table_reg = zip(table_1, table_2)
	table_sic = zip(table_3, table_4)

	toppings = Topping.objects.all()

	sub_large = Sub.objects.filter(size__iexact="Large")
	sub_small = Sub.objects.filter(size__iexact="Small")
	sub = zip(sub_small, sub_large)

	sub_extra = SubExtra.objects.all()


	context = {
		"pizza_r_style": Pizza.objects.values('style').distinct(),
		"pizza_list": table_reg,
		"pizza_list2": table_sic,
		"toppings": toppings,
		"subs": sub,
		"subextras": sub_extra,
	}

	return render(request, "Orders/index.html", context)

def platter(request):

	#platter = Platter.objects.all().order_by('name')
	platter_large = Platter.objects.filter(size__iexact="Large")
	platter_small = Platter.objects.filter(size__iexact="Small")

	platter = zip(platter_small, platter_large)

	context = {
	"platters": platter,
	}

	return render(request, "Orders/platter.html", context)

def cart(request):
	#check for POST Request
	if request.method == 'POST':
		#remove cart item request
		if 'remove-cart' in request.POST:

			remove_id = request.POST['remove']
			PizzaOrder.objects.filter(pk=remove_id).delete()

			return HttpResponseRedirect(reverse("cart"))

		#add pizza to cart
		elif 'pizza-form' in request.POST:

			current_user = request.user
			item = request.POST['item']
			topping = request.POST['topping']
			topping_1 = request.POST['topping-1']
			topping_2 = request.POST['topping-2']
			topping_3 = request.POST['topping-3']
			size = request.POST['size']
			price = request.POST['price']

			#for key in request.POST:
			    #print(key)
			cart = PizzaOrder(user=current_user, style=item, toppings=topping, topping_1=topping_1, topping_2=topping_2, topping_3=topping_3, size=size, price=price)
			cart.save()

			cart_2 = Cart(user=current_user, pizza_order=cart)
			cart_2.save()

			return HttpResponseRedirect(reverse("cart"))

		#add sub to cart	
		elif 'sub-form' in request.POST:

			current_user = request.user
			item = request.POST['item']
			topping = request.POST['topping']
			extra_1 = request.POST['extra-1']
			extra_2 = request.POST['extra-2']
			extra_3 = request.POST['extra-3']
			extra_4 = request.POST['extra-4']
			size = request.POST['size']
			price = request.POST['price']

			#for key in request.POST:
			    #print(key)
			cart = PizzaOrder(user=current_user, style=item, toppings=topping, extra_1=extra_1, extra_2=extra_2, extra_3=extra_3, extra_4=extra_4,  size=size, price=price)
			cart.save()

			cart_2 = Cart(user=current_user, pizza_order=cart)
			cart_2.save()

			return HttpResponseRedirect(reverse("cart"))
		#add platter
		elif 'platter-form' in request.POST:

			current_user = request.user
			item = request.POST['item']
			topping = request.POST['topping']
			size = request.POST['size']
			price = request.POST['price']

			#for key in request.POST:
			    #print(key)
			cart = PizzaOrder(user=current_user, style=item, toppings=topping, size=size, price=price)
			cart.save()

			cart_2 = Cart(user=current_user, pizza_order=cart)
			cart_2.save()

			return HttpResponseRedirect(reverse("cart"))

		elif 'cart-order' in request.POST:

			current_user = request.user
			orders = Cart.objects.filter(user__exact=current_user, ordered=False)
			#total orders for order
			total_orders = Cart.objects.filter(ordered=True, user=current_user).count()
			
			#update cart table
			for ordered in orders:
				Cart.objects.filter(pk=ordered.id).update(ordered=True)


			#update orders table
			
			for order in orders:
				order_cart = Order(user=current_user, items=order)
				order_cart.save()
			
			


			return HttpResponseRedirect(reverse("cart"))

	#get cart for logged in user	
	if request.user.is_authenticated:
		order = Cart.objects.filter(user__exact=request.user)
		context = {
			'carts': order,
		}
		return render(request, "Orders/order.html", context)

	return render(request, "Orders/order.html")

def adminOrder(request):
	if request.user.is_staff:

		order_pending = Order.objects.filter(status__iexact="complete")
		pending_users = Order.objects.filter(status__iexact="pending").values_list('user__username', flat=True).distinct()
		order_user = Order.objects.values_list('user__username', flat=True).distinct()
		print(pending_users)


		order_pending_2 = []
		for ous in pending_users:
			case ={'user': ous, 'items': Order.objects.filter(user__username=ous, status__iexact="pending")} 
			order_pending_2.append(case)



		context = {
			'pending': order_pending,
			'user_orders': order_user,
			'pending_2': order_pending_2,
		}

		if request.method == 'POST':
			if 'status_change' in request.POST:
				order_id = request.POST['order-id']
				status_update = request.POST['status']

				s = Order.objects.get(pk=order_id)
				s.status = status_update
				s.save()

				return HttpResponseRedirect(reverse("order"))

		return render(request, "Orders/order_admin.html", context)


		

		
	return render(request, "Orders/order_admin.html")





