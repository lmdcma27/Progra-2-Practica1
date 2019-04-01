from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    carnet = models.CharField(max_length=9)
    correo = models.EmailField(max_length=50)
    cui = models.CharField(max_length=30)
    contra = models.CharField(max_length=50)
    carrera = ( ('00', 'Licenciatura en Matemática'),
        ('01', 'Licenciatura en Física'),)
    profesion = models.CharField(max_length=2, choices=carrera)

    def _str__(self):
        return self.nombre
    