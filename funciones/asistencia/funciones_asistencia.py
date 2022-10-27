from flask import render_template
from data_base import database as mongodb
from forms.ASISTENCIA.asistencia import Asistencia

DB = mongodb.dbConecction()

def AsistenciaDB():
    titulo = "Asistencia"
    asistenciaDB = DB['asistencia']
    asistencia = asistenciaDB.find()
    return render_template('/ADMINISTRADOR/asistencia/base_datos.html',titulo=titulo,asistencia=asistencia)