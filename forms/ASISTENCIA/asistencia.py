class Asistencia:
    def __init__(self, identificador, nombre, fecha, inicio, Operativo, puesto, fin, activo):
        self.identificador = identificador
        self.nombre = nombre
        self.fecha = fecha
        self.inicio = inicio
        self.Operativo = Operativo
        self.puesto = puesto
        self.fin = fin
        self.activo = activo

    def datosAsistenciaJson(self):
        return {
            'identificador': self.identificador,
            'Nombre': self.nombre,
            'Fecha': self.fecha,
            'Inicio': self.inicio,
            'Estado': self.Operativo,
            'Puesto': self.puesto,
            'Fin': self.fin,
            'Activo': self.activo
        }
