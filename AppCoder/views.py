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

def familia_formulario(request):
    
    if request.method == 'POST':
        familiar_formulario = Familia(request.POST)

        if familiar_formulario.is_valid():

            data = familiar_formulario.cleaned_data

            familiar1 = Familiar(nombre=data.get('nombre'), edad=data.get('edad'))
                
            familiar1.save()

        return redirect('AppCoderInicio')
        
    contexto = {
        'form': Familia()
}

    return render(request, 'familia_Formulario.html', contexto)

def busqueda_familia(request):
    
    contexto = {
        'form': BusquedaFamiliaFormulario(),
    }

    return render(request, 'busqueda_familia.html', contexto)

def busqueda_familia_post(request):
          
    edad = request.GET.get('edad')

    nombres = Familiar.objects.filter(edad__icontains=edad)
    contexto = {
        'nombres': nombres
    }

    return render(request, 'familiar_filtrado.html', contexto)

def mascota_formulario(request):
    
    if request.method == 'POST':
        mascotas_formulario = Mascota(request.POST)
        
        if mascotas_formulario.is_valid():
            
            data = mascotas_formulario.cleaned_data
            
            mascota1 = Mascotas(animal=data.get('animal'), edad=data.get('edad'))
            
            mascota1.save()
        
        return redirect('AppCoderInicio')
    
    contexto = {
        'form': Mascota()
    }

    return render(request, 'mascotasFormulario.html', contexto)

def busqueda_mascota(request):
    
    contexto = {
        'form': BusquedaMascotaFormulario(),
    }
    
    return render(request, 'busqueda_mascota.html', contexto)

def busqueda_mascota_post(request):
    
    animal = request.GET.get('animal')
    
    mascota = Mascotas.objects.filter(animal__icontains=animal)
    contexto = {
        'mascotas': mascota
    }
    
    return render(request, 'mascota_filtrado.html', contexto)