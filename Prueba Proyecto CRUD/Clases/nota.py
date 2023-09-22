# Definimos la clase nota
class Nota:
    # Atributos
    def __init__(self, dni_alumno, codigo_asignatura, calificacion):
        self.dni_alumno = dni_alumno
        self.codigo_asignatura = codigo_asignatura
        self.calificacion = calificacion
    # Diccionario de la clasec nota
    def to_dict(self):
        return {
            "dni_alumno": self.dni_alumno,
            "codigo_asignatura": self.codigo_asignatura,
            "calificacion": self.calificacion
        }




