from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string

menu = [
    {"title": "Главная страница", "path_name": "main", "text": "IT'S MAIN PAGE :P)"},
    {"title": "Поиск элемента из БД", "path_name": "search_element"},
    {"title": "Показать все элементы из БД", "path_name": "all_elements"}
]


def index(request):
    data = {
        "menu": menu,
        "page": menu[0]
    }
    return render(request, "app1/index.html", context=data)


def search_element(request):
    data = {
        "menu": menu,
        "page": menu[1]
    }
    return render(request, "app1/search_element.html", context=data)


def all_elements(request):
    data = {
        "menu": menu,
        "page": menu[2]
    }
    return render(request, "app1/all_elements.html", context=data)


def page_not_found(request, exception=None):  # error page
    return HttpResponse("<h1>page not found :з</h1>")
