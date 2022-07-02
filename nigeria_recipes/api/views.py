from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView, 
    CreateAPIView, 
    DestroyAPIView, 
    UpdateAPIView)

class ListMealView(ListAPIView):
    pass

class  AddMealView(CreateAPIView):
    pass

class MealDetailView(RetrieveAPIView):
    pass

class MealIngredientsView(ListMealView):
    pass

class RemoveMealView(DestroyAPIView):
    pass
class UpdateMealView(UpdateAPIView):
    pass

class RateMealView(APIView):
    pass

class ShareMealView(APIView):
    pass