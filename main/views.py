from django.http import HttpResponse
from django.shortcuts import render

from kondicionery.models import Categories

def index(request):

    categories = Categories.objects.all()

    data = {
        'title' : 'Климатические системы и оборудования',
        'categories' : categories,
    }

    return render(request, 'main/index.html', data)

def dostavka(request):
    data = {
        'title' : 'Доставка по Санкт-Петербургу и Ленинградской области'
    }
    return render(request, 'main/dostavka.html', data)