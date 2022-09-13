from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', inicio, name='AppCoderInicio'),
    path('herencias/', herencias, name='Herencias'),
    path('curso_formulario/', curso_formulario, name='CursoFormulario'),
    path('BusquedaCamada/', busqueda_camada , name='BusquedaCamada'),
    path('busqueda_camada_post/', busqueda_camada_post , name='BusquedaCamadaPost'),

]