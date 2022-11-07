from flask import render_template, session, request
from data_base import database as mongodb
from werkzeug.security import generate_password_hash


DB = mongodb.dbConecction()

def InfoPerfil():
    titulo = 'Informacion administrador'
    AdministradorDB = DB['administrador']
    Administrador = AdministradorDB.find_one({'correo':session['usuario-administrador']})
    return render_template('/ADMINISTRADOR/info_perfil/informacion_admin.html',titulo = titulo, administrador = Administrador)

def Actualizar_password(key,campo):
    AdministradorDB = DB['administrador']
    dato=request.form['dato']
    if dato:
        dato = generate_password_hash(dato, method = 'sha256')
        AdministradorDB.update_one({'correo':key},{'$set':{campo:dato}})
        print(dato)
    return InfoPerfil()      