from django import forms

class FileForm(forms.Form):
    file=forms.FileField(label="file")

class CategoriaForm(forms.Form):
    ide=forms.CharField(label="ide")
    nombre=forms.CharField(label="nombre")
    descripcion=forms.CharField(label="descripcion")
    cargatrabajo=forms.CharField(label="cargatrabajo")
    
class ConfiguracionForm(forms.Form):
    ide=forms.CharField(label="ide")
    nombre=forms.CharField(label="nombre")
    descripcion=forms.CharField(label="descripcion")
    recursosconfiguracion=forms.CharField(label="recursosconfiguracion")
    
class RecursoForm(forms.Form):
    ide=forms.CharField(label="ide")
    nombre=forms.CharField(label="nombre")
    abreviatura=forms.CharField(label="abreviatura")
    metrica=forms.CharField(label="metrica")
    tipo=forms.CharField(label="tipo")
    valorxhora=forms.CharField(label="valorxhora")

class ClienteForm(forms.Form):
    nit=forms.CharField(label="nit")
    nombre=forms.CharField(label="nombre")
    usuario=forms.CharField(label="usuario")
    clave=forms.CharField(label="clave")
    direccion=forms.CharField(label="direccion")
    correo=forms.CharField(label="correo")
    
class InstanciaForm(forms.Form):
    ide=forms.CharField(label="ide")
    idconfiguracion=forms.CharField(label="idconfiguracion")
    nombre=forms.CharField(label="nombre")
    fechainicio=forms.CharField(label="fechainicio")
    estado=forms.CharField(label="estado")
    fechafinal=forms.CharField(label="fechafinal")
    