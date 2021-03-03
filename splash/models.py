import uuid
import json
from django.db import models

PRODUCT_CATEGORIES = [
	(1, 'Concrete'),
	(2, 'Sound Control'),
	(3, 'Concrete Topping'),
	(4, 'Finish')
]

# Create your models here.
def product_logo_path(instance, filename):
	return '{0}-logo.{1}'.format(instance.slug, filename.split('.')[-1])

def product_graphic_path(instance, filename):
	return '{0}-graphic.{1}'.format(instance.slug, filename.split('.')[-1])

class Product(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	category = models.IntegerField(choices=PRODUCT_CATEGORIES)
	description = models.TextField()
	details = models.JSONField(default=list, blank=True, null=True)
	data_sheet = models.URLField(blank=True, null=True)
	logo = models.ImageField(upload_to=product_logo_path, blank=True, null=True)
	graphic = models.ImageField(upload_to=product_graphic_path, blank=True, null=True)

class Project(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	description = models.TextField()
	details = models.JSONField(default=list, blank=True, null=True)
	logo = models.ImageField(upload_to=product_logo_path, blank=True, null=True)

class ProjectImage(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL, related_name='images')
	image = models.ImageField(upload_to='uploads/')
	alt = models.TextField(blank=True, null=True)