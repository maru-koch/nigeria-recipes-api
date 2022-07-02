from uuid import uuid5
from django.db import models
from django.forms import UUIDField

# Create your models here.
class Ingredients(models.Model):
    name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Preparation(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)

class Meal(models.Model):
    id = models.UUIDField(primary_key=True)
    image = models.ImageField(upload_to="images")
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
    description = models.TextField(max_lengt=500)
    ingredients = models.ManyToManyField(Ingredients, null=True, blank=True, related_name="meals")
    preparation = models.TextField(Preparation, max_lengt=500)

    def __str__(self):
        return self.title


