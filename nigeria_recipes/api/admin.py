from django.contrib import admin

# Register your models here.
from .models import Food, Ingredients, Preparation, Category

admin.site.register(Food)
admin.site.register(Ingredients)
admin.site.register(Preparation)
admin.site.register(Category)