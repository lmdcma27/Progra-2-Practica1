from django.db import models
from apps.registro.models import Usuario
# Create your models here.
class Archivos(models.Model):
    password = models.CharField(max_length=50)
    archivo =models.FileField(upload_to='', null = True, blank=True)
    propietario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
    texto = models.TextField()
    