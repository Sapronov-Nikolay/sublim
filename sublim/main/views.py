
import sublim
# from . import views
# from django.http import HttpResponse
# from .forms import *
from django.shortcuts import render
from .models import Good, Kategory
from .forms import GoodForm, SearchForm


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
            "topnavset": get_top_menu("/"),
            "navset": get_menu("/"),
        }
    )


# Пытаемся сделать поисковик. Он будет искать нам искомое по частям слов и буквосочетаниям
'''СПИСЫВАЕМ С ЭТОГО!!!
def add_task(request):
    if request.method == 'POST':
        print(request.POST)
        task_data = TaskForm(request.POST)
        if task_data.is_valid():
             print(task_data.cleaned_data)
    task_form = TaskForm()
    return render(            
        request,         
        'tasklist/form.html',
        {
           'task_form_auto_gen': task_form
        }
    )
'''


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
