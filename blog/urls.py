# from django.urls import path, re_path
# from blog import views
#
# urlpatterns = [
#     path('', views.index),
#     path('about/', views.about, kwargs={'name': 'Tom', 'age': 38}),
#     re_path(r'^contact/', views.contact),
#     re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)/', views.user),
#     re_path(r'^user/(?P<name>\D+)/', views.user),
#     re_path(r'^user/', views.user),
# ]

from django.urls import path, include
from blog import views

product_patterns = [
    path("", views.products),
    path("comments/", views.comments),
    path("questions/", views.questions),
]

urlpatterns = [
    path("", views.index),
    path("products/<int:id>/", include(product_patterns)),
]