
from flask import Blueprint, request, render_template, redirect, url_for, flash
from tkinter.filedialog import askopenfile
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

@app.route('/login/<user>/<password>' )
def login(user=None,password=None):
    res=gestor.obtener_usuario(user,password)
    if res==None:
        return '{"data":false,"message":"Tu usuario no existe o es invalido"}'
    return '{"data":true,"message":"Bienvenido"}'
    
@app.route('/login')
def login2():
    json=request.get_json()
    res=gestor.obtener_usuario(json['user'],json['password'])
    if res==None:
        return jsonify({"data":False,"message":"Tu usuario no existe o es invalido"})
    return jsonify({"data":True,"message":"Bienvenido"})
    
 #RUTAS CORRESPONDIENTES PARA NUESTRO BACKEND: ACA IRAN ENLAZADAS LAS FUNCIONES CREADAS CON POO   
    
@app.route('/config', methods=["POST"])
def config():
    if request.method=='POST':
        archivoConfig=askopenfile()
    
    
        return jsonify({
            "succes":True
        })
    
@app.route("/listado", methods=["POST"])
def listado():
    
    archivoListado=askopenfile()
    print(archivoListado)
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
    return jsonify({
        "succes":True
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