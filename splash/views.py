from django.shortcuts import render, redirect
from .models import *

import os

# Create your views here.
def index(request):
	return render(request, 'index.html')

def about_us(request):
	team = [{
		'name': 'Eric Meissner',
		'title': 'President',
		'url': 'img/team/eric.png'
	},{
		'name': 'Peter Kosinski',
		'title': 'Vice President',
		'url': 'img/team/peter.png'
	},{
		'name': 'Chantai Sircy',
		'title': 'Vice President of Sales and Marketing',
		'url': 'img/team/chantai.png'
	},{
		'name': 'Matt Rugg',
		'title': 'Waterproofing Superintendent',
		'url': 'img/team/matt.png'
	}]
	return render(request, 'about.html', {'team':team})

def contact_us(request):
	return render(request, 'contact.html')

def projects(request):
	projects = Project.objects.all()
	return render(request, 'projects.html', {'projects':projects})

def srv_concrete(request):
	products = Product.objects.filter(category=1)
	return render(request, 'srv-concrete.html', {'products':products})

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
	data = os.getenv('TEST')
	return render(request, 'template.html', {'data':data})

## Error handling
def handler404(request, exception):
	return render(request, 'handler404.html', status=404)

def handler500(request):
	return render(request, 'handler500.html', status=500)