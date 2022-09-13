from statistics import mode
from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()

class Curso(models.Model):
    camada = models.IntegerField()
    nombre = models.CharField(max_length=10)

class Mascotas(models.Model):
    animal = models.CharField(max_length=50)
    edad = models.IntegerField()