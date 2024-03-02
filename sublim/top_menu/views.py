from django.shortcuts import render

from main.models import *




menu = [{'main': "Главная"},
        {'goods': "Товары"}, 
        {'cart': "Корзина"}, "О сублимировании", "Регистрация"
]
def index(request):
    posts = Good.objects.all()
    contexttop = {
        'Document': 'главное на сегодня',
        'posts': posts,   # отображает модель с товарами
        'text': 'Содержимое',
        'menu': menu    # Отображает меню в index.html значение {{m}} class="top_menu"
    }
    return render(request, 'top_menu/index.html', context=contexttop)

