
import sublim
# from . import views
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from .models import Good, Category
from .forms import GoodForm  # , CartForm
from django.core.paginator import Paginator


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
    if request.method == 'POST':
        # print(request.POST)
        # print(request.POST['poisk'])
        goods = []
        search = request.POST['poisk'].lower()
        for good in Good.objects.all():
            if good.namegood.lower() == search:
                goods.append(good)

    categories = map(
        lambda cat: Category.objects.get(pk=cat['category_id']),
        Good.objects.order_by().values('category_id').distinct()
    )
    return render(
        request,
        "main/tovars.html",

        # Kонтекст передаваемых переменных
        {

            "Товары": goods,
            "summa": 0,  # summa,,
            "categories": categories,
            "navset": get_menu("/shop") # меню "Акции" "Магазин" "Доставка" "Рецепты" "О сублимировании"

        }
    )

'''
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
'''

def pokupki(request):
    print("\n\n\nkuku", request.method, request.GET)
    categories = map(
        lambda cat: Category.objects.get(pk=cat['category_id']),
        Good.objects.order_by().values('category_id').distinct()
    )
    goods = Good.objects.all()
    cat_id = 1
    if 'category' in request.GET:
        print('Катя: ', request.GET['category'])
        cat_id = Category.objects.get(
                categoriya=request.GET['category']).id
        goods = Good.objects.filter(
            category_id=cat_id)

    return render(
        request,
        "main/tovars.html",

        # Kонтекст передаваемых переменных
        {
            "Товары": goods,
            "cat_selected": cat_id,
            "navset": get_menu("/shop"),
            "categories": categories,
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

def pagen(request):
    contact_list = Good.objects.all()
    paginator = Paginator(contact_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/tovars.html', {'page_obj': page_obj })

# "Это для приветственного окна"
def privet(request):
    return render(request, 'main/privet.html', {"navset": get_menu("/")})


# Функция для поиска товаров по категориям
def show_category(request, category_slug=""):
    categories = map(
        lambda cat: Category.objects.get(pk=cat['category_id']),
        Good.objects.order_by().values('category_id').distinct()
    )
    print(categories)
    #if category_slug:
    #    Good = get_object_or_404(Category, slug=category_slug)
        
    return render(
        request,
        'main/categories.html',
        {
            "navset": get_menu("/"),
            "categories": categories
            })


# Для отображения сообщения вместо нехнической информайии при DEBUG = False в settings.py
def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>') 