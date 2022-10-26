from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home, name="front-home"),
    
    path('crearcategoria/', views.crearCategoria, name="crearcategoria"),
    path('crearrecurso/', views.crearRecurso, name="crearrecurso"),
    path('crearconfiguracion/', views.crearConfiguracion, name="crearconfiguracion"),
    path('crearcliente/', views.crearCliente, name="crearcliente"),
    path('crearinstancia/', views.crearInstancia, name="crearinstancia"),
    
    path("load/",views.load, name="load"),
    path("eliminarDatos/",views.eliminarDatos, name="eliminarDatos"),
]