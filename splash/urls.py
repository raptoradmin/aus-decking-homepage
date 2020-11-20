from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('gypsum-concrete', views.srv_concrete, name='srv_concrete'),
	path('sound-control', views.srv_sound, name='srv_sound'),
	path('concrete-topping', views.srv_topping, name='srv_topping'),
	path('specialty-finishes', views.srv_finish, name='srv_finish'),
	path('product/<slug:slug>', views.product_details, name='product'),
	path('template', views.test, name='template'),
]