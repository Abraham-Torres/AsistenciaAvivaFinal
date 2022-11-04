from flask import render_template
from data_base import database as mongodb

DB = mongodb.dbConecction()

def Home():
    titulo="Inicio"
    ActivosDB = DB['puestos']
    act= False
    activo = ActivosDB.count_documents({})
    return render_template('/index.html',titulo=titulo,activo=activo)

    