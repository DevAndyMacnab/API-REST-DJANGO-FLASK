from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask import Flask, Flask,request
from flask import *
from flask.json import jsonify
from flask_cors import CORS
from gestor import Gestor

app=Flask(__name__)
app.config["DEBUG"]=True
CORS(app)
gestor=Gestor()

@app.route('/')
def home():
    return "Los alumnos de IPC2 B van a ganar"

    
 #RUTAS CORRESPONDIENTES PARA NUESTRO BACKEND: ACA IRAN ENLAZADAS LAS FUNCIONES CREADAS CON POO   
    
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
    return jsonify({
        "succes":True
    })
    
@app.route("/crearrecurso", methods=["POST"])
def crearRecurso():
    return jsonify({
        "succes":True
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
    return jsonify({
        "succes":True
    })
@app.route("/crearcliente", methods=["POST"])
def crearCliente():
    return jsonify({
        "succes":True
    })
    
@app.route("/crearinstancia", methods=["POST"])
def crearInstancia():
    return jsonify({
        "succes":True
    })
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

    
    




if __name__ == "__main__":
    app.run(debug=True)