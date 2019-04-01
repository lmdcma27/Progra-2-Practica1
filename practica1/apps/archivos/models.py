from django.db import models

# Create your models here.
class Archivos(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    archivo =models.FileField(upload_to='media/', null = True, blank=True)

    def __str__(self):
        return self.name