from django import views
from django.urls import path
from top_menu import views

urlpatterns = [
    path('recipies/', views.recipies, name='recipies'),
]