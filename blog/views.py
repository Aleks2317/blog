from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse('<h2>Главная<h2>')


def about(requests):
    return HttpResponse('<h2>О сайте<h2>')


def contact(request):
    return HttpResponse('<h2>Контакты</h2>')

