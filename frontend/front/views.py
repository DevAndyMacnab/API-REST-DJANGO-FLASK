import json
from urllib import response
from django.shortcuts import render, redirect
from flask import jsonify
from .forms import ClienteForm, ConfiguracionForm, FileConfigForm, CategoriaForm, InstanciaForm, RecursoForm, FileIntakeForm
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



def cargarConfiguraciones(request):
    ctx={
        "content":None,
        "response":None,
        "cantidades":None
    }
    if request.method=='POST':
        form=FileConfigForm(request.POST,request.FILES)
        if form.is_valid():
            f=request.FILES["file"] 
            xml_binary=f.read()
            print(xml_binary)
            print(f.read())
            xml=xml_binary.decode('utf-8')
            ctx["content"]=xml
            response=requests.post(endpoint+"agregarconfiguraciones",data=xml)
            if response.ok:
                ctx["response"]=response.json()
                ctx["cantidades"]=response.json()
                print(ctx["cantidades"])
            else:
                ctx["response"]="Hubo algun tipo de error en la ejecucion"
        else:
            return render(request,"cargar.html")
    return render(request, 'carga.html', ctx)

def cargarconsumos(request):
    ctx={
        "content":None,
        "response":None
    }
    if request.method=='POST':
        form=FileConfigForm(request.POST,request.FILES)
        if form.is_valid():
            f=request.FILES["file"] 
            xml_binary=f.read()
            print(xml_binary)
            print(f.read())
            xml=xml_binary.decode('utf-8')
            ctx["content"]=xml
            response=requests.post(endpoint+"agregarconsumos",data=xml)
            if response.ok:
                ctx["response"]="Archivo XML de consumos se ha cargado correctamente"   
            else:
                ctx["response"]="Hubo algun tipo de error en la ejecucion"
        else:
            return render(request,"cargarconsumos.html")
    return render(request, 'cargarconsumos.html', ctx)

def eliminarDatos(request):
    if request.method=='GET':
        response=requests.get(endpoint+"resetear")
        if response.ok:
            return redirect("/home")
        
def ayuda(request):
    return render(request, 'ayuda.html')