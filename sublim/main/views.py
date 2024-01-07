
import sublim
#from . import views
#from django.http import HttpResponse
#from .forms import *
from django.shortcuts import render
from .models import Good, Kategory

def get_menu(active):
    result = []
    for elem in sublim.urls.navset:
        if elem['url'] == active:
            elem['active'] = True
        result.append(elem)
    return result

def index(request):
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
            "navset": get_menu("/")

        }
    )

def pokupki(request):
    summa = 0
    goods = Good.objects.all()
    for g in goods:
        summa += g.price

    return render(
        request,
        "main/menu.html",

        # Kонтекст передаваемых переменных
        {

            "Товары": goods,
            "summa": summa,
            "navset": get_menu("/shop")

        }
    )
