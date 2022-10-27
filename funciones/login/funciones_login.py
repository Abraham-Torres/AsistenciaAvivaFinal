from flask import render_template, session, flash, request, redirect
from data_base import database as mongodb
from werkzeug.security import generate_password_hash, check_password_hash

DB = mongodb.dbConecction()

def IniciarSesion():
    titulo="iniciar sesion"
    return render_template('/ADMINISTRADOR/login/login.html',titulo=titulo)

def AutenticacionAdmins():
    correo = request.form['correo']
    password = request.form['password']
    usuario = False
    if correo and password:
        Administrador = DB['administrador']
        AdminRecibido = Administrador.find_one({'correo':correo})
        if AdminRecibido:
            if(check_password_hash(AdminRecibido['password'], password)==True):
                session['usuario-administrador'] = AdminRecibido['correo']
                usuario = True
                session.pop('usuario-puesto',None)
                return redirect('/HOME')    
            elif(check_password_hash(AdminRecibido['password'],password)==False):
                flash('Error: Contraseña incorrecta')
        elif usuario == False:
            flash('Error: El usuario no existe')   
        return IniciarSesion()
    flash('Por favor llene todos los campos')      
    return IniciarSesion()