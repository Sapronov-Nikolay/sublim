"""
URL configuration for sublim project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('top_menu/', include('top_menu.urls')),
]

# def get_top_menu(active): во views.py
topnavset = [
    {'url': '/catalog',                  'text':  'Каталог',              'active': False},
    {'url': '/basket',                   'text':  'Корзина',              'active': False},
    {'url': '/persacc',                  'text':  'Личный кабинет',       'active': False},
    {'url': '/registration',             'text':  'Регистрация',          'active': False},

]
# def get_menu(active): во views.py
navset = [
    {'url': '/',                         'text': 'Главная',               'active': False},
    {'url': '/shop',                     'text': 'Магазин',               'active': False},
    {'url': '/delivery',                 'text': 'Доставка',              'active': False},
    {'url': '/recipies',                 'text': 'Рецепты',               'active': False},
    {'url': '/sublim',                   'text': 'О сублимировании',      'active': False},
]
# def add_cart(request): во views.py
cartnavset = [
    {'url': '/cart',                     'text': 'Заказать',              'active': False},
]
# во views.py
leftmenu = [
    {'url': '/categores',                'text': 'Категории',             'active': False},
    {'url': '/meat',                     'text': 'Мясные',                'active': False},
    {'url': '/vegetable',                'text': 'Овощные',               'active': False},
    {'url': '/fruit',                    'text': 'Фруктовые',             'active': False},
    {'url': '/berry',                    'text': 'Ягодные',               'active': False},
    {'url': '/mixtures',                 'text': 'Смеси',                 'active': False},
    {'url': '/coffee_chicory',           'text': 'Кофе (цикорий)',        'active': False},
    {'url': '/mushrooms',                'text': 'Грибы',                 'active': False},
    {'url': '/seasoning',                'text': 'Приправы',              'active': False},
    {'url': '/confectionary_products',   'text': 'Кондитерские изделия',  'active': False},
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
