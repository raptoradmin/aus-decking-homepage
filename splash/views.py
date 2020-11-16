from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')

def srv_concrete(request):
	return render(request, 'srv-concrete.html')

def srv_sound(request):
	return render(request, 'srv-sound.html')

def srv_topping(request):
	return render(request, 'srv-topping.html')

def srv_finish(request):
	return render(request, 'srv-finish.html')

def test(request):
	return render(request, 'template.html')