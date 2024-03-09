
import sublim
# from . import views
from django.http import HttpResponse, HttpResponseNotFound
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .models import Good, Category
from .forms import GoodForm  # , CartForm


def get_top_menu(active):
    result = []
    for elem in sublim.urls.topnavset:
        if elem['url'] == active:
            elem['active'] = True
        result.append(elem)
    return result


def get_menu(active):
    result = []
    for elem in sublim.urls.navset:
        if elem['url'] == active:
            elem['active'] = True
        result.append(elem)
    return result


def get_leftmenu(active):
    result = []
    for elem in sublim.urls.leftmenu:
        if elem['url'] == active:
            elem['active'] = True
        result.append(elem)
    return result


def index(request):
    #    all_goods = Good.objects.filter(namegood)
    result = ""

    categ = ""
    for a in Category.objects.all():
        categ += a.categoriya

    return render(
        request,
        "main/index.html",

        # Kонтекст передаваемых переменных
        {
            "Товар": Good.objects.all(), "Категории": categ,
            "search": get_top_menu("/"),
            "navset": get_menu("/"), # меню "Акции" "Магазин" "Доставка" "Рецепты" "О сублимировании"
            "leftmenu": get_leftmenu("/"),
        }
    )


def search(request):
    # goods = Good.objects.all()  # filter(namegood=input()) # , 'картофель'])
    goods = []
    if request.method == 'POST':
        # print(request.POST)
        # print(request.POST['poisk'])
        goods = Good.objects.filter(namegood=request.POST['poisk'])

    categ = ""
    for a in Category.objects.all():
        categ += a.categoriya

    return render(
        request,
        "main/tovars.html",

        # Kонтекст передаваемых переменных
        {

            "Товары": goods,
            "summa": 0,  # summa,
            "navset": get_menu("/shop") # меню "Акции" "Магазин" "Доставка" "Рецепты" "О сублимировании"

        }
    )


def add_good(request):
    if request.method == 'POST':
        print(request.POST)
        good_poisk = GoodForm(request.POST)
        if good_poisk.is_valid():
            print(good_poisk.namegood)
    good_form = GoodForm()  # ругается на это
    return render(
        render(

        )
    )


def pokupki(request):
    summa = 0
    goods = Good.objects.all()
    for g in goods:
        summa += g.price

    return render(
        request,
        "main/tovars.html",

        # Kонтекст передаваемых переменных
        {
            "Товары": goods,
            "summa": summa,
            "navset": get_menu("/shop")
        }
    )


def add_cart(request):
    cart_form = []
    total_sum = 0
    if request.method == 'POST':
        for key in request.POST:
            print(key, request.POST[key])
            if key[1:].isdigit() and key[0] == 'i':
                t = Good.objects.get(pk=int(key[1:]))
                print(t, t.namegood, request.POST[key])
                if float(request.POST[key]) > 0:
                    cart_form.append({
                        # 'picture': t.picture,
                        'namegood': t.namegood,
                        'price': t.price,
                        'kolvo': request.POST[key],
                        'picture': t.picture,
                        'summa': int(float(t.price) * float(request.POST[key])),
                    })
                    total_sum += float(t.price) * float(request.POST[key])
    return render(
        request, 'main/cart.html',
        {
            'cart_form_auto_gen': cart_form,
            "navset": get_menu("/"),
            'total_sum': int(total_sum)
        }
    )

# "Это для приветственного окна"
def privet(request):
    return render(request, 'main/privet.html', {"navset": get_menu("/")})


# Функция для поиска товаров по категориям
            # ЦЕЛЫЙ ДЕНЬ ЮЗАЮ ТУТ ВСЁ И НИЧЕГО НЕ ВЫХОДИТ
def show_category(request, category_slug):
    Good = get_object_or_404(Category, slug=category_slug)
    slug = Good.CATEGORY.all()
    return render(request, 'main/categories.html', {"navset": get_menu("/")}, slug)


# Для отображения сообщения вместо нехнической информайии при DEBUG = False в settings.py
def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>') 