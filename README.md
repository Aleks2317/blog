# Создать проект Django
- **django-admin startproject Course_FirstProject .** \
Точка в данной команде указывает на то, что проект будет создан в этой же папке


- **python manage.py runserver** \
запустим наш сервер


## Структура проекта выглядит так

> **Cource_FirstProject/:**  это папка является контейнером проекта, 
который состоит из следующих ниже файлов:
>>- **__init__.py:** пустой файл, который сообщает Python, 
<br> что каталог Cource_FirstProject нужно трактовать как пакет Python.
>> - **asgi.py:** конфигурация для выполнения проекта в качестве приложения, работающего по протоколу интерфейса шлюза 
асинхронного сервера (ASGI) с ASGI-совместимыми веб-серверами. ASGI – это новый стандарт Python для асинхронных веб-серверов и приложений.
>> - **settings.py:** здесь указаны настроечные параметры и конфигурация проекта и содержатся изначальные параметры со 
значениями, используемыми по умолчанию.
>> - **urls.py:** место, где располагаются ваши шаблоны URL-адресов. Каждый URL-адрес, который определен здесь, 
  соотносится с представлением.
>>- **wsgi.py** — с помощью этого файла приложение может работать с веб-сервером по протоколу WSGI.

> **manage.py:** это утилита командной строки, используемая для взаимодействия с проектом. Редактировать этот файл не 
  требуется;

> **.venv:** это созданный каталог с нашим виртуальным окружением.


# применим миграции:


- **python manage.py migrate**

# settings.py

- **DEBUG** – это булев параметр, который включает и выключает режим отладки проекта. Если его значение установлено 
равным True, то Django будет отображать подробные страницы ошибок в случаях, когда приложение выдает не перехваченное исключение. При переходе в производственную среду следует помнить о том, что необходимо устанавливать его значение равным False. Никогда не развертывайте свой сайт в производственной среде с включенной отладкой, поскольку вы предоставите конфиденциальные данные, связанные с проектом.

- **ALLOWED_HOSTS** – не применяется при включенном режиме отладки или при выполнении тестов. При перенесении своего 
  сайта в производственную среду и установке параметра DEBUG равным False в этот настроечный параметр следует добавлять свои домен/хост, чтобы разрешить ему раздавать ваш сайт Django.
- **INSTALLED_APPS** – это параметр, который придется редактировать во всех проектах. Он сообщает Django о приложениях, 
  которые для этого проекта являются активными(установленными). По умолчанию Django добавляет следующие ниже приложения:
>> - **django.contrib.admin:** раздел администрирования.
>> - **django.contrib.auth:** фреймворк аутентификации.
>> - **django.contrib.contenttypes:** фреймворк типов контента.
>> - **django.contrib.sessions:** фреймворк сеансов.
>> - **django.contrib.messages:** фреймворк сообщений.
>> - **django.contrib.staticfiles:** фреймворк управления статическими файлами.
- **MIDDLEWARE** – подлежащие исполнению промежуточные программные компоненты.
- **ROOT_URLCONF** – указывает модуль Python, в котором определены шаблоны корневых URL-адресов приложения.
- **DATABASES** – словарь, содержащий настроечные параметры всех баз данных, которые будут использоваться в проекте. 
  Всегда должна существовать база данных, которая будет использоваться по умолчанию. В стандартной конфигурации используется база данных SQLite3, если не указана иная.
- **LANGUAGE_CODE** – определяет заранее заданный языковой код этого сайта Django.
- **USE_TZ** – сообщает Django, что нужно активировать/деактивировать поддержку часовых поясов. Django поставляется 
  вместе с поддержкой дат и времен с учетом часовых поясов. Этот настроечный параметр имеет значение по умолчанию  True после создания нового проекта, с помощью команды управления startproject.

Все настроечные параметры и их значения, которые используются по умолчанию, 
можно увидеть на [странице](https://docs.djangoproject.com/en/5.0/ref/settings/).

## созданием приложения

>**python manage.py startapp blog**

## Структура приложенния 

>> **__init__.py:**  пустой  файл,  который  сообщает  Python,  что  каталог blog нужно трактовать как пакет Python;
> 
>> **admin.py:** здесь вы регистрируете модели, чтобы управлять ими через веб-интерфейс админ панели нашего сайта;
>
>> **apps.py:** содержит главную конфигурацию приложения blog;
>
>>**migrations:** этот каталог будет содержать миграции базы данных приложения. Миграции позволяют Django отслеживать 
изменения модели соответствующим образом синхронизировать базу данных. Указанный каталог содержит пустой файл __init__.py;
>
>>**models.py:** содержит относимые к приложению модели данных. Если вы не будете использовать модели в своем 
приложении, его можно удалить;
>
>>**tests.py:** здесь можно добавлять относимые к приложению тесты;
>
>>**views.py:** здесь расположена логика приложения; каждое представление получает HTTP-запрос, обрабатывает его и 
возвращает ответ.

Когда структура приложения готова, можно приступать к разработке представлений нашего приложения.

# Работа с представлениями и адресами.

settings.py.


В текстовом редакторе откройте этот файл и прокрутите ниже до INSTALLED_APPS, где вы увидите шесть встроенных приложений Django. Добавим blog.apps.BlogConfig в самый низ:
>INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig' # наше новое приложение
]

## следующим шагом будет создание нашего первого представления. Начнем с обновления файла views.py в нашем приложении 
blog, чтобы он выглядел следующим образом:

blog/views.py:
>from django.http import HttpResponse
> 
> 
>def homepageview(request): \
>    return HttpResponse('Hello, World!')

## Далее нам нужно настроить наши URL-адреса. Создайте новый файл urls.py в приложении blog. Затем обновите его 
следующим кодом:

blog/urls.py:

>rom django.urls import path\
>from .views import homepageview
>
>urlpatterns = [path('', homepageview, name='home'), ]

### Наш добавленный маршрут состоит из трех частей:

1. Шаблон URL адреса для корневой директории сайта ''.

2. Используемая функция-представление homepageview.

3. Имя маршрута home, это необязательный именованный параметр name функции path.

## Последний шаг - это обновление нашего файла Cource_FirstProject/urls.py.

Cource_FirstProject/urls.py:

>from django.contrib import admin\
>from django.urls import path, include  # new
>
>urlpatterns = [
>    path('admin/', admin.site.urls),\
>    path('', include('blog.urls')),  # new 
>]

