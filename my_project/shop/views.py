from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Главная страница"""
    return render(request, 'index.html', {
        'title': 'Главная страница',
        'message': 'Это главная страница нашего вебприложения'
    })


def about(request):
    """Описание проекта"""
    return HttpResponse('<h1>Описание проекта</h1>')


def catalog(request):
    """Каталог мороженого"""
    return HttpResponse('<h1>Каталог мороженого</h1>')


def product_detail(request, product_id):
    """Страница отдельного товара"""
    return HttpResponse(f'<h1>Название товара {product_id}</h1>')
