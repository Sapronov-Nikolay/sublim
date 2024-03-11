
from django.urls import path
from django.urls import include
from main import views

urlpatterns = [
    path('', views.privet, name='menu'),
    path('search/', views.search, name='search'),
    path('shop/', views.pokupki),
    path('cart/', views.add_cart),
    path('index/', views.index),
    path('categories/', views.show_category, name='category'),
    #path('categories/<slug:category_slug>/', views.show_category, name='category'),
]
