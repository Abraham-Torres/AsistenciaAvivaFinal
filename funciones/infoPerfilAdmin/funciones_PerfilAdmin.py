from flask import render_template, session
from data_base import database as mongodb


DB = mongodb.dbConecction()

def InfoPerfil():
    titulo = 'Informacion administrador'
    AdministradorDB = DB['administrador']
    Administrador = AdministradorDB.find_one({'correo':session['usuario-administrador']})
    return render_template('/ADMINISTRADOR/info_perfil/informacion_admin.html',titulo = titulo, administrador = Administrador)