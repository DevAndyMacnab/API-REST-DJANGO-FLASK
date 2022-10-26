import json
from django.shortcuts import render
from .forms import FileForm, CategoriaForm
import requests

# Create your views here.
endpoint="http://127.0.0.1:5000/"

def home(request):
    
    return render(request, 'home.html')

def add(request):
    if request.method=='POST':
        form=CategoriaForm(request.POST)
        if form.is_valid():
            json_data=form.cleaned_data
            response=requests.post(endpoint + 'crearcategoria',json=json_data)
            if response.ok:
                return render(request, 'add.html',{'form':form})
        print("Si se cumplio")
        return render(request, 'add.html',{'form':form})
        
    return render(request, 'add.html')


def load(request):
    return render(request, 'carga.html')