from django.shortcuts import render
from django.http import HttpResponse

#from sublim.main.views import get_menu






def recipies(request):
    return render(
        request,
        'top_menu/recipies.html',
            {
                #"navset": get_menu("/"),
            }
        )

