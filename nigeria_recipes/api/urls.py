from django.urls import path
from .views import (ListMealView, 
MealDetailView, 
MealIngredientsView, 
RemoveMealView, 
UpdateMealView, 
RateMealView, 
ShareMealView)

urlpatterns =[
    path('meals', ListMealView.as_view()),
    path('meals/add', ListMealView.as_view()),
    path('meals/<pk>',MealDetailView.as_view()),
    path('meals/ingredients', MealIngredientsView.as_view()),
    path('meals/<pk>', RemoveMealView.as_view()),
    path('meals/<pk>', UpdateMealView.as_view()),
    path('meals/<pk>/rating', RateMealView.as_view()),
    path('meals/<pk>/share', ShareMealView.as_view()),
]