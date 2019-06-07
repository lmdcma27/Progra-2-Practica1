from django.urls import path
from . import views
urlpatterns = [   
   path('', views.registro, name='registro'),
   path('direccion/unica/creada/para/validar/cuenta/atraves/de/correo/electronico/', views.validacion, name = 'validacion'),
]