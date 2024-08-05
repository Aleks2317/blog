from django.shortcuts import HttpResponse


def homepageview(request):
    return HttpResponse('Hello, World!')
