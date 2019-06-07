from django.urls import path 

from . import views

urlpatterns = [
    path('lexer/', views.lexer, name = 'lexer'),
    path('resultado/<str:cadena>/', views.resultado, name = 'resultado'),
]