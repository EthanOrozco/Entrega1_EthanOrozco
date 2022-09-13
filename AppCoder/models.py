from statistics import mode
from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    cumpleaños = models.DateField()
    edad = models.IntegerField()

class Curso(models.Model):
    camada = models.IntegerField()
    nombre = models.CharField(max_length=10)

class Mascotas(models.Model):
    edad = models.IntegerField()
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)