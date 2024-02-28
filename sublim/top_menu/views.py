from django.shortcuts import render

from main.models import *




menu = ["Главная", "| Товары", "| Корзина", "| О сублимировании", "| Регистрация"]
def index(request):
    posts = Good.objects.all()
    return render(request, 'top_menu/index.html', 
        {
        'Document': 'главное на сегодня',
        'posts': posts,   # отображает модель с товарами
        'text': 'Содержимое',
        'menu': menu    # Отображает меню в index.html значение {{m}} class="top_menu"
        }
    )

