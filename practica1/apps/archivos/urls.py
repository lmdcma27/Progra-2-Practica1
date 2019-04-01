from django.urls import path
from . import views

urlpatterns = [
    path('subida_archivos/', views.archivar, name = 'archivar'),
    path('<str:nombre>/archivos_subidos/', views.archivos_subidos, name = 'archivos_subidos'),
    path('error_usuario/', views.error_usuario, name = 'error_usuario'),
    path('error_extension/', views.error_extension, name = 'error_extension'),
]
