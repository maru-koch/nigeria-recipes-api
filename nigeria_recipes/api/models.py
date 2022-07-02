from uuid import uuid5
from django.db import models
from django.forms import UUIDField, uuid5

# Create your models here.
class Ingredients(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Meal(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid5)
    image = models.ImageField(upload_to="images")
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title

class Recipes(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.SET_NULL)
    ingredient=models.ManyToManyField(Ingredients)
    quantity=models.IntegerField()
    def __str__(self):
        return f"{self.meal} recipes"

class Preparation(models.Model):
    meal = models.ForeignKey(Meal)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)

    def __str__(self):
        return self.title

