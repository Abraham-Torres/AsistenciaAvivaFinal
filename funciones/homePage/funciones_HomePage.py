from flask import render_template
def Home():
    titulo="Inicio"
    return render_template('/index.html',titulo=titulo)