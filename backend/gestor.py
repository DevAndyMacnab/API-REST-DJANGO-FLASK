from Categoria.categoria import Categoria
from Categoria.configuracion import Configuracion
from Categoria.recurso import Recurso
from Cliente.cliente import Cliente
from Cliente.instancia import Instancia


import json
from xml.dom.minidom import Element
import xml.etree.ElementTree as ET
from flask import Flask, Flask,request
from flask.json import jsonify

class Gestor:
    def __init__(self):
        self.clientes=[]
        self.instancias=[]
        self.categorias=[]
        self.configuraciones=[]
        self.recursos=[]
        
    def agregarCategoria(self,ide,nombre,descripcion,cargaTrabajo):
        nuevo=Categoria(ide,nombre,descripcion,cargaTrabajo)
        self.categorias.append(nuevo)
        return True
    
    def agregarConfiguracion(self,ide,nombre,descripcion,cargaTrabajo):
        nuevo=Configuracion(ide,nombre,descripcion,cargaTrabajo)
        self.configuraciones.append(nuevo)
        return True
    
    def agregarRecurso(self,ide,nombre,descripcion,cargaTrabajo):
        nuevo=Recurso(ide,nombre,descripcion,cargaTrabajo)
        self.recursos.append(nuevo)
        return True
    
    def agregarCliente(self,ide,nombre,descripcion,cargaTrabajo):
        nuevo=Cliente(ide,nombre,descripcion,cargaTrabajo)
        self.clientes.append(nuevo)
        return True
    
    def agregarInstancia(self,ide,nombre,descripcion,cargaTrabajo):
        nuevo=Instancia(ide,nombre,descripcion,cargaTrabajo)
        self.instancias.append(nuevo)
        return True
        
         

    
    
