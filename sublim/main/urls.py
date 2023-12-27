from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings

    
urlpatterns = [
    path('', views.index), # Добавлено направление
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)