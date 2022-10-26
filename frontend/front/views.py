import json
from urllib import response
from django.shortcuts import render
from .forms import ClienteForm, ConfiguracionForm, FileForm, CategoriaForm, InstanciaForm, RecursoForm
import requests

# Create your views here.
endpoint="http://127.0.0.1:5000/"

def home(request):
    contexto={
        "datos":[]
    }
    try:
        response=requests.get(endpoint+"consultardatos")
        datos=response.json()
        contexto["datos"]=datos
    except:
        print("Error en la API ")
        
    return render(request, 'home.html',contexto)

def crearCategoria(request):
    if request.method=='POST':
        form=CategoriaForm(request.POST)
        if form.is_valid():
            json_data=form.cleaned_data
            response=requests.post(endpoint + 'crearcategoria',json=json_data)
            if response.ok:
                return render(request, 'crearcategoria.html',{'form':form})
        print("Si se cumplio")
        return render(request, 'crearcategoria.html',{'form':form})
        
    return render(request, 'crearcategoria.html')


def crearRecurso(request):
    if request.method=='POST':
        form=RecursoForm(request.POST)
        if form.is_valid():
            json_data=form.cleaned_data
            response=requests.post(endpoint + 'crearrecurso',json=json_data)
            if response.ok:
                return render(request, 'crearrecurso.html',{'form':form})
        print("Si se cumplio")
        return render(request, 'crearrecurso.html',{'form':form})
        
    return render(request, 'crearrecurso.html')

def crearConfiguracion(request):
    if request.method=='POST':
        form=ConfiguracionForm(request.POST)
        if form.is_valid():
            json_data=form.cleaned_data
            response=requests.post(endpoint + 'crearconfiguracion',json=json_data)
            if response.ok:
                return render(request, 'crearconfiguracion.html',{'form':form})
        print("Si se cumplio")
        return render(request, 'crearconfiguracion.html',{'form':form})
        
    return render(request, 'crearconfiguracion.html')


def crearCliente(request):
    if request.method=='POST':
        form=ClienteForm(request.POST)
        if form.is_valid():
            json_data=form.cleaned_data
            response=requests.post(endpoint + 'crearcliente',json=json_data)
            if response.ok:
                return render(request, 'crearcliente.html',{'form':form})
        print("Si se cumplio")
        return render(request, 'crearcliente.html',{'form':form})
        
    return render(request, 'crearcliente.html')

def crearInstancia(request):
    if request.method=='POST':
        form=InstanciaForm(request.POST)
        if form.is_valid():
            json_data=form.cleaned_data
            response=requests.post(endpoint + 'crearinstancia',json=json_data)
            if response.ok:
                return render(request, 'crearinstancia.html',{'form':form})
        print("Si se cumplio")
        return render(request, 'crearinstancia.html',{'form':form})
        
    return render(request, 'crearinstancia.html')


def load(request):
    return render(request, 'carga.html')