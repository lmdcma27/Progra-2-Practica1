from django.db import models

# Create your models here.

class Regex(models.Model):

    regex = models.CharField(max_length=150, primary_key=True)
    
       
