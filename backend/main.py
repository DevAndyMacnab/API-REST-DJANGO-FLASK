from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask import Flask, Flask,request
from flask import *
from flask.json import jsonify
from flask_cors import CORS
from gestor import Gestor
from xml.etree import ElementTree as ET

app=Flask(__name__)
app.config["DEBUG"]=True
CORS(app)
gestor=Gestor()

@app.route('/')
def home():
    return "Los alumnos de IPC2 B van a ganar"

    
 #RUTAS CORRESPONDIENTES PARA NUESTRO BACKEND: ACA IRAN ENLAZADAS LAS FUNCIONES CREADAS CON POO   
    
#CARGADO DE DATOS MASIVOS POR MEDIO DE ARCHIVOS XML
@app.route('/config', methods=["POST"])
def config():
    if request.method=='POST':
        
        return jsonify({
            "succes":True
        })
    
@app.route("/listado", methods=["POST"])
def listado():
    
    return jsonify({
        "succes":True
    })
    
@app.route("/consultardatos", methods=["GET"])
def consultarDatos():
    consulta=gestor.obtenerDatos()
    return jsonify(consulta),200

    
    #RUTAS PARA INGRESAR DATOS DE MANERA INDIVIDUAL DEPENDIENDO LA CATEGORIA REQUERIDA
@app.route("/crearrecurso", methods=["POST"])
def crearRecurso():
    json=request.get_json()
    gestor.agregarRecurso(json["ide"],json["nombre"],json["abreviatura"],json["metrica"],json["tipo"],json["valorxhora"])
    return jsonify({
        "succes":True,
        "message":"Se ha creado el recurso nuevo correctamente"
    })
    
@app.route("/crearcategoria", methods=["POST"])
def crearCategoria():
    
    json=request.get_json()
    gestor.agregarCategoria(json["ide"],json["nombre"],json["descripcion"],json["cargatrabajo"])
    return jsonify({
        "ID":json["ide"],
        "Nombre":json["nombre"],
        "Descripcion":json["descripcion"],
        "Carga de Trabajo":json["cargatrabajo"],
        "message":"Se ha creado la categoria correctamente!"
                    })
    
    
@app.route("/crearconfiguracion", methods=["POST"])
def crearConfiguracion():
    
    json=request.get_json()
    gestor.agregarConfiguracion(json["ide"],json["nombre"],json["descripcion"],json["recursosconfiguracion"])
    return jsonify({
        "succes":True,
        "message":"Se ha creado la configuracion correctamente"
    })
    
    
@app.route("/crearcliente", methods=["POST"])
def crearCliente():
    json=request.get_json()
    gestor.agregarCliente(json["nit"],json["nombre"],json["usuario"],json["clave"],json["direccion"],json["correo"])
    return jsonify({
        "succes":True,
        "message":"Se ha creado el cliente nuevo correctamente"
    })
    
    
@app.route("/crearinstancia", methods=["POST"])
def crearInstancia():
    json=request.get_json()
    gestor.agregarInstancia(json["ide"],json["idconfiguracion"],json["nombre"],json["fechainicio"],json["estado"],json["fechafinal"])
    return jsonify({
        "succes":True,
        "message":"Se ha creado la instancia correctamente"
    })
    
    
    #FUNCIONES U OPERACIONES DEL SISTEMA
@app.route("/generarfactura", methods=["POST"])
def generarFactura():
    consulta=gestor.generarFactura()

    return jsonify(consulta),200

@app.route("/reportes", methods=["GET"])
def reportes():
    gestor.generarReporte()
    
    
    return jsonify({
        "succes":True
    })

    
@app.route("/resetear",methods=["GET"])
def resetear():
    gestor.resetearDatos()
    return jsonify({"message":"Los datos se han borrado correctamente"})

@app.route("/agregarconfiguraciones",methods=["POST"])
def agregarconfiguraciones():
    xmlConfig=request.data.decode("utf-8")
    raiz=ET.XML(xmlConfig)
    Recursos=[]
    mensaje=""
    contrecursos=0
    contcategorias=0
    contconfiguraciones=0
    contclientes=0
    continstancias=0
    for cosa in raiz:
        
        clientes=cosa.findall("cliente")
        
        for cliente in clientes:
            contclientes+=1
            nit=cliente.attrib["nit"]
            nombre=cliente.find("nombre").text
            usuario=cliente.find("usuario").text
            clave=cliente.find("clave").text
            direccion=cliente.find("direccion").text
            correo=cliente.find("correoElectronico").text
            gestor.agregarCliente(nit,nombre,usuario,clave,direccion,correo)
            print(contclientes)
            for instancias in cliente:
                
                instancia=instancias.findall("instancia")
                for inst in instancia:
                    continstancias+=1
                    ide=inst.attrib["id"]
                    idConfig=inst.find("idConfiguracion").text
                    nombre=inst.find("nombre").text
                    fechaInicio=inst.find("fechaInicio").text
                    estado=inst.find("estado").text
                    fechaFinal=inst.find("fechaFinal").text
                    gestor.agregarInstancia(ide,idConfig,nombre,fechaInicio,estado,fechaFinal)
            print("instancias")
            print(continstancias)
                       
    for element in raiz:
        
        
        
        recursos= element.findall("recurso")
        for recurso in recursos:
            contrecursos+=1
            ide=recurso.attrib["id"]
            nombre=recurso.find("nombre").text
            abreviatura=recurso.find("abreviatura").text
            metrica=recurso.find("metrica").text
            tipo=recurso.find("tipo").text
            valorxhora=recurso.find("valorXhora").text
            gestor.agregarRecurso(ide,nombre,abreviatura,metrica,tipo,valorxhora)
        print("RECURSOSS")
        print(contrecursos)    
            
        categorias= element.findall("categoria")
        for categoria in categorias:
            
            ide=categoria.attrib["id"]
            nombre=categoria.find("nombre").text
            descripcion=categoria.find("descripcion").text
            cargatrabajo=categoria.find("cargaTrabajo").text
            
            print("CATEGORIASSS")
            contcategorias+=1
            
            gestor.agregarCategoria(ide,nombre,descripcion,cargatrabajo)
            
            for configuraciones in categoria:
                
                configuracion=configuraciones.findall("configuracion")
                for elemento in configuracion:
                    print("CONFIGURACIONESS")
                    
                    contconfiguraciones+=1
                    print(contconfiguraciones)
                    ide=elemento.attrib["id"]
                    nombre=elemento.find("nombre").text
                    descripcion=elemento.find("descripcion").text
                    print("CONFIGURACIONES" , ide, nombre, descripcion)
                    mensaje=""
                    for source in elemento:
                        idrecursos=source.findall("recurso")
                        for ele in idrecursos:
                            ide=ele.attrib["id"]
                            recurso=ele.text
                            Recursos.append({
                                "ide":ide,
                                "cantidad":recurso
                            })
                            mensaje+= "ID Recurso: " + ide +"," + "Cantidad Recurso: " +recurso 
                            
                            print(Recursos)
                            
                    gestor.agregarConfiguracion(ide,nombre,descripcion,mensaje)
                 
    return jsonify("Se han cargado: "+str(contrecursos) + " recursos, " + str(contcategorias) + " categorias, " + str(contconfiguraciones) + " configuraciones, " + str(contclientes) + " clientes, " 
                    + str(continstancias) + " instancias.")  
    
    
     
@app.route("/agregarconsumos",methods=["POST"])
def agregarConsumos():
    xmlConsumos=request.data.decode("utf-8")
    raiz=ET.XML(xmlConsumos)
    contconsumos=0
    for element in raiz:
        contconsumos+=1
        nit=element.attrib["nitCliente"]
        ide=element.attrib["idInstancia"]
        tiempo=element.find("tiempo").text
        fechahora=element.find("fechaHora").text
        print("CONSUMOS "+ nit + ide)
        gestor.agregarConsumos(nit,ide,tiempo,fechahora)
        
    return jsonify("Se han cargado: " + str(contconsumos) + " consumos")
    


if __name__ == "__main__":
    app.run(debug=True)