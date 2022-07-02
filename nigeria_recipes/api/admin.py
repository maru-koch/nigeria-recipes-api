from django.contrib import admin

# Register your models here.
from .models import Meal, Ingredient, Preparation, Category

admin.site.register(Meal)
admin.site.register(Ingredient)
admin.site.register(Preparation)
admin.site.register(Category)