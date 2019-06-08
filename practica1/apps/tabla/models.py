from django.db import models
from apps.regex.models import Regex
# Create your models here.
class Tabla(models.Model):
    tabla = models.ForeignKey(Regex, null=True, blank=True, on_delete=models.CASCADE)