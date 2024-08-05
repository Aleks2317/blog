from django.urls import path, re_path
from blog import views

urlpatterns = [
    re_path(r'^contact/', views.contact),
    re_path(r'^about/', views.about),
    path('', views.index),
]
