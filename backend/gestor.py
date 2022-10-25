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
    
    def agregarConfiguracion(self,ide,nombre,descripcion,recursosConfiguracion):
        nuevo=Configuracion(ide,nombre,descripcion,recursosConfiguracion)
        self.configuraciones.append(nuevo)
        return True
    
    def agregarRecurso(self,ide,nombre,abreviatura,metrica,tipo,valorXHora):
        nuevo=Recurso(ide,nombre,abreviatura,metrica,tipo,valorXHora)
        self.recursos.append(nuevo)
        return True
    
    def agregarCliente(self,nit,nombre,usuario,clave,direccion,correo):
        nuevo=Cliente(nit,nombre,usuario,clave,direccion,correo)
        self.clientes.append(nuevo)
        return True
    
    def agregarInstancia(self,ide,idConfiguracion,nombre,fechaInicio,estado,fechaFinal):
        nuevo=Instancia(ide,idConfiguracion,nombre,fechaInicio,estado,fechaFinal)
        self.instancias.append(nuevo)
        return True
        
         

    
    
