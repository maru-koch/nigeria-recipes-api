from django.shortcuts import render
from rest_framework.views import APIView

#: Generic views
from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView, 
    CreateAPIView, 
    DestroyAPIView, 
    UpdateAPIView)

#: Serializers
from .serializer import (
    MealsSerializer, 
    IngredientSerializer, 
    CategorySerializer, 
    PreparationSerializer)

#: Models
from .models import (
    Meal, 
    Category, 
    Ingredients, 
    Preparation)

class ListMealView(ListAPIView):
    serializer_class = MealsSerializer
    queryset = Meal.objects.all()

class  AddMealView(CreateAPIView):
    serializer_class = MealsSerializer
    queryset = Meal.objects.all()

class MealDetailView(RetrieveAPIView):
    serializer_class = MealsSerializer
    queryset = Meal.objects.all()

class MealIngredientsView(ListMealView):
    serializer_class = IngredientSerializer
    queryset = Ingredients.objects.all()

class RemoveMealView(DestroyAPIView):
    serializer_class = MealsSerializer
    queryset = Meal.objects.all()

class UpdateMealView(UpdateAPIView):
    serializer_class = MealsSerializer
    queryset = Meal.objects.all()

class RateMealView(APIView):
    pass

class ShareMealView(APIView):
    pass