# Definimos la clase alumno
class Alumno:
    # Atributos
    def __init__(self, dni, nombre, apellido, edad, fecha_nac):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.fecha_nac = fecha_nac
    #    self.notas = [] # Lista de notas que tendra cada alumno
    # Funcion para agregar una nota al alumno
    #def __agregar_nota(slef, nota):
    #    self.notas.append(nota)
    # Diccionario de alumno
    def to_dict(self):
        return {
            "dni": self.dni,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "fecha_nac": self.fecha_nac
            #"notas": [nota.to_dict() for nota in self.notas]
        }     





