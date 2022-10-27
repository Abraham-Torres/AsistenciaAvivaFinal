#IMPORTAMOS TODAS LAS LIBRERIAS QUE NECESITAREMOS
from flask import Flask

'''
Primero impprtamos de la carpeta funciones, la carpeta servidor (que contiene el archivo funciones_Servidor.py)
y le damos un alias.
Dentro de funciones_Servidor importamos render_template (este solo se importara donde sera usado no aqui en el index)
definimos una funcion, que esta va a contener todo lo que muestre el html (render_template)
Despues definimos otra funcion donde recibira los parametros establecidos
y retornamos el alis del archivo, ademas de la funcion que hicimos dentro de funciones_Servidor
'''
import funciones.servidor.funciones_Servidor as fun_serv
import funciones.homePage.funciones_HomePage as fun_home
import funciones.puestos.funciones_puestos as fun_puest
import funciones.puestosOperativos.funciones_puestosOperativos as fun_op
import funciones.estadosOperativos.funciones_estadosOperativos as fun_status


app=Flask(__name__)


#FUNCION DE HOMEPAGE
@app.route('/HOME')
def HomePage():
    return fun_home.Home()

#**********************************************************************************************

#FUNCION PUESTO(FORMULARIO)
@app.route('/REGISTRAR-PUESTO')
def FormularioPuesto():
    return fun_puest.Formulario()

#FUNCION AGREGAR PUESTO
@app.route('/NUEVO-PUESTO',methods=['POST'])
def NuevoPuesto():
    return fun_puest.Nuevo()    
    
#FUNCION DE BD PUESTOS
@app.route('/BASE-DATOS-PUESTO')
def BaseDatos():
    return fun_puest.PuestoDb()

#FUNCION DE OPERACIONES PUESTO
@app.route('/OPERACIONES-PUESTO')
def Operaciones():
    return fun_puest.Operaciones_Puesto()

#FUNCION DE INFORMACION PUESTO
@app.route('/INFORMACION-PUESTO<key>')
def Informacion(key):
    return fun_puest.Informacion_Puesto(key)    

#FUNCION DE INFORMACION/ELIMINAR
@app.route('/ELIMINAR-PUESTO<key>')
def Eliminar_Puesto(key):
    return fun_puest.Eliminar_Puesto(key)

#FUNCION DE INFORMACION/ACTUALIZAR
@app.route('/ACTUALIZAR-PUESTO/<key>,<campo>',methods=['POST'])
def Actualizar_Puesto(key,campo):
    return fun_puest.Actualizar_puesto(key,campo)

#**********************************************************************************************
# FUNCION  DE DB DE PUESTOS OPERATIVOS
@app.route('/BASE-DATOS-PUESTOS-OPERATIVOS')
def BaseDatosOperativos():
    return fun_op.PuestoOperativoDb()

#FUNCION DE AGREGAR PUESTOS OPERATIVOS
@app.route('/NUEVO-PUESTO-OPERATIVO',methods = ['POST'])
def NuevoOperativo():
    return fun_op.NuevoPuestoOperativo()  

#FUNCION DE ELIMINAR PUESTO OPERATIVOS 
@app.route('/ELIMINAR-PUESTO-OPERATIVOS<key>')
def EliminarOperativo(key):
    return fun_op.EliminarPuestoOperativo(key)

#**********************************************************************************************   

#FUNCION DE DB DE ESTADOS OPERATIVOS
@app.route('/BASE-DATOS-ESTADOS-OPERATIVOS')
def BaseDatosEstados():
    return fun_status.EstadosOperativos()

#FUNCION DE AGREGAR NUEVO ESTADO OPERATIVO
@app.route('/NUEVO-ESTADO-OPERATIVO', methods=['POST'])  
def NuevoEstadoOperativo():
    return fun_status.NuevoEstado()  

#FUNCION DE ELIMINAR ESTADOS OPERATIVOS
@app.route('/ELIMINAR-ESTADO-OPERATIVO<key>')   
def EliminarEstadoOperativo(key):
    return fun_status.EliminarEstado(key) 

#**********************************************************************************************

#FUNCION DE PAGINA NO ENCONTRADA    
def Pagina_no_encontrada(error):
        return fun_serv.Error_404(error)

#**********************************************************************************************


#HACEMOS EL CONSTRUCTOR.
if __name__=='__main__':
    app.register_error_handler(404, Pagina_no_encontrada)
    app.run(host="0.0.0.0",debug=True)
    #CONFIGURAMOS EL HOST PARA QUE PUEDA ACCEDER DE CUALQUIER IP
    #Y TAMBIEN EL MODO DEBUG PARA VER LOS CAMBIOS EN TIEMPO REAL.