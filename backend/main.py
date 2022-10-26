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
    return jsonify({
        "succes":True
    })

@app.route("/reportes", methods=["GET"])
def reportes():
    return jsonify({
        "succes":True
    })
@app.route("/ayuda", methods=["GET"])
def ayuda():
    return jsonify({
        "succes":True
    })
    
@app.route("/resetear",methods=["GET"])
def resetear():
    gestor.resetearDatos()
    return jsonify({"message":"Los datos se han borrado correctamente"})

@app.route("/agregarconfiguraciones",methods=["POST"])
def agregarConfiguraciones():
    xmlConfig=request.data.decode("utf-8")
    raiz=ET.XML(xmlConfig)
    
    for element in raiz:
        print(element.attrib)
    
@app.route("/agregarconsumos",methods=["POST"])
def agregarConsumos():
    xmlConsumos=request.data.decode("utf-8")
    raiz=ET.XML(xmlConsumos)
    
    for element in raiz:
        print( element.attrib)


if __name__ == "__main__":
    app.run(debug=True)