from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
	return render(request, 'index.html')

def srv_concrete(request):
	return render(request, 'srv-concrete.html')

def srv_sound(request):
	products = Product.objects.filter(category=2)
	return render(request, 'srv-sound.html', {'products':products})

def srv_topping(request):
	return render(request, 'srv-topping.html')

def srv_finish(request):
	return render(request, 'srv-finish.html')

def product_details(request, slug):
	product = Product.objects.get(slug=slug)
	if not product:
		return redirect('index')
	return render(request, 'product.html', {'p':product})

def test(request):
	return render(request, 'template.html')