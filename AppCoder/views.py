from cmath import inf
import datetime
from urllib import request
from django.shortcuts import render, redirect  
from AppCoder.models import *
from AppCoder.forms import *
# Create your views here.

def inicio(request):
    
    return render(request, 'index.html')

def herencias(request):

    return render(request, 'herencias.html')

def Formularios(request):

    contexto = {
        'form': Familia()
    }
    
    return render(request, 'formulario.html', contexto)

def curso_formulario(request):

    if request.method == 'POST':
        mi_formulario = CursoForm(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            curso1 = Curso(nombre=data.get('nombre'), camada=data.get('camada'))
                
            curso1.save()

        return redirect('AppCoderInicio')
        
    contexto = {
        'form': CursoForm()
}

    return render(request, 'cursoFormulario.html', contexto)

def busqueda_camada(request):
    
    contexto = {
        'form': BusquedaCamadaFormulario(),
    }

    return render(request, 'busqueda_camada.html', contexto)

def busqueda_camada_post(request):
        
    camada = request.GET.get('camada')

    cursos = Curso.objects.filter(camada__icontains=camada)
    contexto = {
        'cursos': cursos
    }

    return render(request, 'curso_filtrado.html', contexto)