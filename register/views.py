from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from .forms import RegisterForm

# Create your views here.

def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()

			return redirect("order")
	else:
		form = RegisterForm()
	
	context = {
	"form": form,
	}
	return render(request, "register/register.html", context )