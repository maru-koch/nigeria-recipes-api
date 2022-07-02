from django.contrib import admin

# Register your models here.
from .models import Meal, Ingredients, Preparation, Category

admin.site.register(Meal)
admin.site.register(Ingredients)
admin.site.register(Preparation)
admin.site.register(Category)