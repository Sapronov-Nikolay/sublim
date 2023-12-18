from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import Good
# Create your views here.
def index(request):
    result = ""
    tovar = ""
    for i in Good.objects.all():
        tovar += i.namegood
    return render(request, 'main/index.html',
                  {

                    "Товары": Good.objects.all(),
                    #"navset": get_menu("/shopping")
                    }
    )

