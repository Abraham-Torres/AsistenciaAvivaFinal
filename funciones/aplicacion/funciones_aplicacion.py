from flask import render_template, request, session, redirect, flash
from data_base import database as mongodb
from werkzeug.security import check_password_hash
from forms.ASISTENCIA.asistencia import Asistencia 
import time

DB = mongodb.dbConecction()

def iniciarSesionApp():
    titulo='Iniciar sesion empleado'
    return render_template('/APLICACION/login/login.html',titulo=titulo)

def CerrarSesionEmpleado():
    session.pop('usuario-empleado',None)
    return redirect('/INICIAR-SESION-EMPLEADO')    

def AutenticacionEmpleado():
    correo = request.form['correo']
    password = request.form['password']
    usuario = False
    if correo and password:
        Empleado = DB['puestos']
        EmpleadoRecibido = Empleado.find_one({'correo':correo})
        if EmpleadoRecibido:
            if(check_password_hash(EmpleadoRecibido['password'],password)==True):
                session['usuario-empleado'] = EmpleadoRecibido['correo']
                usuario = True
                session.pop('usuario-administrador', None)
                return redirect ('/HOME-APP')
            elif(check_password_hash(EmpleadoRecibido['password'],password)==False):
                flash ('Error: La contraseña es incorrecta')
        elif usuario == False:
            flash('Error: Usuario incorrecto o no existe')
        return iniciarSesionApp()
    flash('No se han insertado datos en el formulario')
    return iniciarSesionApp()                     

def homeAppPage():
    if 'usuario-administrador' in session:
        return redirect('/INICIAR-SESION-EMPLEADO')
    elif 'usuario-empleado' in session:        
        titulo='Incio APP'
        datosPuestoDB = DB['puestos']
        datosEstadoDB = DB['estadoscat']
        Estado = datosEstadoDB.find()
        puestos = datosPuestoDB.find_one({'correo':session['usuario-empleado']})
        return render_template('/APLICACION/index.html',titulo=titulo,Estado=Estado,puestos=puestos)

def AsistenciaApp():
    if 'usuario-administrador' in session:
        return redirect('/INICIAR-SESION-EMPLEADO')
    elif 'usuario-empleado' in session:
         datosPuestoDB = DB['puestos']
         asistenciaDB = DB['asistencia']
         DatosPuesto = datosPuestoDB.find_one({'correo':session['usuario-empleado']})
         nombre = DatosPuesto['nombre']
         fecha = time.strftime('%d-%m-%y')
         puesto = DatosPuesto['tipo_puesto']
         identificador = str(fecha)+str(session['usuario-empleado'])
         operativo = request.form['EstadoOperativo']
         inicio = time.strftime('%X')
         fin = '00:00:00'
         activo = False

         if identificador and nombre and fecha and inicio and operativo and puesto and fin and activo:
            asistencia=Asistencia(identificador, nombre, fecha, inicio, operativo, puesto, fin, activo)
            asistenciaDB.insert_one(asistencia.datosAsistenciaJson())
            return redirect('/HOME-APP')          