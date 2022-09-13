from socket import fromshare
from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class Familia(forms.Form):
    nombre = forms.CharField(max_length=40)
    edad = forms.IntegerField()

class Mascota(forms.Form):
    raza = forms.CharField(max_length=40)
    edad = forms.IntegerField()


class BusquedaCamadaFormulario(forms.Form):
    camada = forms.IntegerField()