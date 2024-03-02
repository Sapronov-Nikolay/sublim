from django import views
from django.urls import path
from top_menu import views

urlpatterns = [
    path('', views.index, name='top_menu'),
    path('shop/', views.index, name='nav')
]