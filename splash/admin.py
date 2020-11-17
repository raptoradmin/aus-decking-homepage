from django.contrib import admin
from django.forms import widgets
from .models import *

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name','slug','category']
	list_filter = ['category']
	search_fields = ('name',)

# Register your models here.
admin.site.register(Product, ProductAdmin)