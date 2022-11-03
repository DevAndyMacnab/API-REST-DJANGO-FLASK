from Categoria.categoria import Categoria
from Categoria.configuracion import Configuracion
from Categoria.recurso import Recurso
from Cliente.cliente import Cliente
from Cliente.instancia import Instancia
from Consumo import Consumo
import json
from xml.dom.minidom import Element
import xml.etree.ElementTree as ET
from flask import Flask, Flask,request
from flask.json import jsonify
import pdfkit
import fitz
class Gestor:
    def __init__(self):
        self.clientes=[]
        self.instancias=[]
        self.categorias=[]
        self.configuraciones=[]
        self.recursos=[]
        self.consumos=[]
        self.json=[]
        
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
        print(self.clientes)
        return True
    
    def agregarInstancia(self,ide,idConfiguracion,nombre,fechaInicio,estado,fechaFinal):
        nuevo=Instancia(ide,idConfiguracion,nombre,fechaInicio,estado,fechaFinal)
        self.instancias.append(nuevo)
        return True
    
    def agregarConsumos(self,nit,ide,tiempo,fechahora):
        nuevo=Consumo(nit,ide,tiempo,fechahora)
        self.consumos.append(nuevo)
        return True
    
    def obtenerDatos(self):
        self.json=[]
        for element in self.recursos:
            recurso={
                "DATO": "RECURSO",
                "ID":element.ide,
                "Nombre":element.nombre,
                "Abreviatura":element.abreviatura,
                "Metrica":element.metrica,
                "Tipo":element.tipo,
                "ValorporHora":element.valorxHora  
            }
            self.json.append(recurso)
            
        for element in self.categorias:
            categoria={
                "DATO": "CATEGORIA",
                "ID":element.ide,
                "Nombre":element.nombre,
                "Descripcion":element.descripcion,
                "CargadeTrabajo":element.cargaTrabajo
                
                
            }
            self.json.append(categoria)
            
        for element in self.configuraciones:
            configuracion={
                "DATO": "CONFIGURACION",
                "ID":element.ide,
                "Nombre":element.nombre,
                "Descripcion":element.descripcion,
                "RecursosdeConfiguracion":element.recursosConfiguracion,
                
                
            }
        
            self.json.append(configuracion)
            

        for element in self.clientes:
            
            cliente={
                "DATO": "CLIENTE",
                "nit":element.nit,
                "Nombre":element.nombre,
                "Usuario":element.usuario,
                "Clave":element.clave,
                "Direccion":element.direccion,
                "Correo":element.correo
            }
            self.json.append(cliente)
            
        for element in self.instancias:
            instancia={
                "DATO": "INSTANCIA",
                "ID":element.ide,
                "IDdeconfiguracion":element.idConfiguracion,
                "Nombre":element.nombre,
                "Fechadeinicio":element.fechaInicio,
                "Estado":element.estado,
                "FechadeFinalizacion":element.fechaFinal 
                
                
            }
            self.json.append(instancia)
            
        for element in self.consumos:
            consumo={
                "DATO":"CONSUMO",
                "ID":element.ide,
                "nit":element.nit,
                "tiempo":element.tiempo,
                "fechahora":element.fechahora
            }
            self.json.append(consumo)
            
            
        
        return self.json
    
    def resetearDatos(self):
        self.instancias=[]
        self.clientes=[]
        self.configuraciones=[]
        self.recursos=[]
        self.categorias=[]
        self.consumos=[]
        
    def generarFactura(self):
        self.mensajes=[]
        print("ENTRAMOS A GENERAR FACTURA")
        self.mensajes.append({
            "message":"Se ha generado la factura correctamente"
        })
        for element in self.clientes:
            
            for consumo in self.consumos:
                print(consumo.nit)
                if consumo.nit==element.nit:
                    print("si estan iguales we felicidades")
                    mensaje={
                        "Cliente": element.nombre,
                        "Usuario": element.usuario,
                        "Instancia":consumo.ide,
                        "Tiempo":consumo.tiempo,
                        "FechaHora":consumo.fechahora
                    }
                    self.mensajes.append(mensaje)

        return self.mensajes
    
    
    def generarReporte(self):
        mensaje=""
        consulta=self.obtenerDatos()
        f=fitz.open()
        pagina=f.new_page()
        posicion=fitz.Point(100,200)
        
        for element in consulta:
           mensaje+= "\n" + str(element.values())
                
            
        msg='''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
        '''
        pagina.insert_text(posicion,mensaje,fontsize=6)
        f.write()
        f.save("prueba.pdf",pretty=True)  
        
        
    
        
    
        
         

    
    
