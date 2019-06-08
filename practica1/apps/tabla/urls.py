from django.urls import path 

from . import views

urlpatterns = [
    path('tabla/', views.tabla, name = 'tabla'),
    path('tabla/<str:re>/', views.expresion, name = 'expresion'),
]
