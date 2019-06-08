from django.urls import path 

from . import views

urlpatterns = [
    path('expresiones/', views.expresiones, name = 'expresoines'),
    path('gramatica/', views.gramatica, name = 'gramatica'),
]
