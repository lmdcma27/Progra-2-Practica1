from django.db import models
from apps.regex.models import Regex
# Create your models here.

class Lexer(models.Model):
    cadena = models.ForeignKey(Regex, null=True, blank=True, on_delete=models.CASCADE)
    texto = models.TextField()