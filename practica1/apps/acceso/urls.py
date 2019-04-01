from django.urls import path
from . import views

urlpatterns = [   
   path('acceso/', views.acceso, name = 'acceso'),
   path('<str:nombre>', views.perfil, name = 'perfil'),
]
