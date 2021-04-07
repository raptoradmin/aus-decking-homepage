from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about-us', views.about_us, name='about_us'),
	path('contact-us', views.contact_us, name='contact_us'),
	path('projects', views.projects, name='projects'),
	path('gypsum-concrete', views.srv_concrete, name='srv_concrete'),
	path('sound-control', views.srv_sound, name='srv_sound'),
	path('concrete-topping', views.srv_topping, name='srv_topping'),
	path('specialty-finishes', views.srv_finish, name='srv_finish'),
	path('product/<slug:slug>', views.product_details, name='product'),
	path('template', views.test, name='template'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.handler404
handler500 = views.handler500