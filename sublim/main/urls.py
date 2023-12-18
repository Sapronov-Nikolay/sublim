from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

    
urlpatterns = [
    path('', views.index), # Добавлено направление
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)