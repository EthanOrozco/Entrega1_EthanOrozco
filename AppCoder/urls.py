from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', inicio, name='AppCoderInicio'),
    path('herencias/', herencias, name='Herencias'),
    path('curso_formulario/', curso_formulario, name='CursoFormulario'),
    path('BusquedaCamada/', busqueda_camada , name='BusquedaCamada'),
    path('busqueda_camada_post/', busqueda_camada_post , name='BusquedaCamadaPost'),
    path('familia_formulario/', familia_formulario, name='FamiliaFormulario'),
    path('Busquedafamilia/', busqueda_familia , name='BusquedaFamilia'),
    path('busqueda_familia_post/', busqueda_familia_post , name='BusquedaFamiliaPost'),
    path('mascota_formulario/', mascota_formulario, name='MascotaFormulario'),
    path('Busquedamascota/', busqueda_mascota , name='BusquedaMascota'),
    path('busqueda_mascota_post/', busqueda_mascota_post , name='BusquedamascotaPost'),

]