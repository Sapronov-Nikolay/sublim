
from django.urls import path
from django.urls import include
from main import views

urlpatterns = [
    path('', views.index),
    path('shop/', views.pokupki),
]
