# from django.shortcuts import HttpResponse
#
#
# def index(request):
#     return HttpResponse('<h2>Главная<h2>')
#
#
# def about(requests, name, age):
#     return HttpResponse(f'''
#     <h2>О пользователе</h2>
#     <p>Имя: {name}</p>
#     <p>Возраст: {age}</p>
# ''')
#
#
# def contact(request):
#     return HttpResponse('<h2>Контакты</h2>')
#
#
# def user(request, name='Undefined', age=0):
#     return HttpResponse(f'<h2>Имя: {name}, Возраст: {age}</h2>')

# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("Главная страница")
#
#
# def products(request, id):
#     return HttpResponse(f"Товар {id}")
#
#
# def comments(request, id):
#     return HttpResponse(f"Комментарии о товаре {id}")
#
#
# def questions(request, id):
#     return HttpResponse(f"Вопросы о товаре {id}")

from django.http import HttpResponse


def index(request):
    return HttpResponse("Главная страница")


def products(request, id):
    return HttpResponse(f"Товар {id}")


def comments(request, id):
    return HttpResponse(f"Комментарии о товаре {id}")


def questions(request, id):
    return HttpResponse(f"Вопросы о товаре {id}")