
from usuario import Usuario
import json
from xml.dom.minidom import Element
import xml.etree.ElementTree as ET
from flask import Flask, Flask,request
from flask.json import jsonify

class Gestor:
    def __init__(self):
        self.usuarios=[]
        self.canciones=[]
        self.usuarios.append(Usuario('Jackeline','Benitez','admin','jacks128'))
        self.usuarios.append(Usuario('Kirby','SuperStar','kirby123','kirby'))

    def obtener_usuarios(self):
        return json.dumps([ob.__dict__ for ob in self.usuarios])

    def obtener_usuario(self,user,password):
        for x in self.usuarios:
            if x.user==user and x.password==password:   
                return x
        return None
    
    
    def entradaConfig(archivo):
        print()