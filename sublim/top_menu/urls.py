from django.urls import path
from top_menu import views

urlpatterns = [
    path('', views.top_menu),
]