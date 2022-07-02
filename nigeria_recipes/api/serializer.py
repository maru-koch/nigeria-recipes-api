from dataclasses import fields
from rest_framework import serializers
from .models import Meal, Ingredients, Category, Preparation

class MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Ingredients
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields = "__all__"

class PreparationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Preparation
        fields = "__all__"