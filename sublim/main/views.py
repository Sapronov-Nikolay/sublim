
import sublim
# from . import views
# from django.http import HttpResponse
# from .forms import *
from django.shortcuts import render
from .models import Good, Kategory
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

    kateg = ""
    for a in Kategory.objects.all():
        kateg += a.kategoriya

    return render(
        request,
        "main/index.html",

        # Kонтекст передаваемых переменных
        {
            "Товар": Good.objects.all(), "Категории": kateg,
            "search": get_top_menu("/"),
            "navset": get_menu("/"),
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

    kateg = ""
    for a in Kategory.objects.all():
        kateg += a.kategoriya

    return render(
        request,
        "main/tovars.html",

        # Kонтекст передаваемых переменных
        {

            "Товары": goods,
            "summa": 0,  # summa,
            "navset": get_menu("/shop")

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
    if request.method == 'POST':
        for key in request.POST:
            if key[1:].isdigit() and key[0] == 'i':
                t = Good.objects.get(pk=int(key[1:]))
                print(t, t.namegood, request.POST[key])
                cart_form.append({
                    'picture': t.picture,
                    'namegood': t.namegood,
                    'price': t.price,
                    'kolvo': request.POST[key],
                    'summa': float(t.price)*float(request.POST[key])
                })
    return render(
        request, 'main/cart.html',
        {
            'cart_form_auto_gen': cart_form
        }
    )


def privet(request):
    return render(request, 'main/privet.html', 
            {
                "mainmenu": get_top_menu("/")
            }
    )