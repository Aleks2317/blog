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

# Параметры строки запроса
# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("<h2>Главная</h2>")
#
#
# def user(request):
#     age = request.GET.get("age")
#     name = request.GET.get("name")
#     return HttpResponse(f"<h2>Имя: {name}, Возраст: {age}</h2>")

# значение по умолчанию в параметрах URLS
#
# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("<h2>Главная</h2>")
#
#
# def user(request):
#     age = request.GET.get("age", 0)
#     name = request.GET.get("name", "Undefined")
#     return HttpResponse(f"<h2>Имя: {name}, Возраст: {age}</h2>")


# Переадресация

# from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
#
#
# def index(request):
#     return HttpResponse("Index")
#
#
# def about(request):
#     return HttpResponse("About")
#
#
# def contact(request):
#     return HttpResponseRedirect("/about")
#
#
# def details(request):
#     return HttpResponsePermanentRedirect("/")


# тправка статусных кодов

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest


def index(request, id):
    people = [None, "Bob", "Sam", "Tom"]
    # если пользователь найден, возвращаем его
    if id in range(1, len(people)):
        return HttpResponse(people[id])
    # если нет, то возвращаем ошибку 404
    else:
        return HttpResponseNotFound("Not Found")


def access(request, age):
    # если возраст НЕ входит в диапазон 1-110, посылаем ошибку 400
    if age not in range(1, 111):
        return HttpResponseBadRequest("Некорректные данные")
    # если возраст больше 17, то доступ разрешен
    if age > 17:
        return HttpResponse("Доступ разрешен")
    # если нет, то возвращаем ошибку 403
    else:
        return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")
