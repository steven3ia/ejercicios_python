# Definimos la clase asignatura
class Asignatura:
    # Atributos
    def __init__(self, codigo, nombre, notas):
        self.codigo = codigo
        self.nombre = nombre
        self.notas = [] # Lista de notas que tendra cada asignatura
    
    # Diccionario de la asignatura
    def to_dict(self):
    return {
        "codigo": self.codigo,
        "nombre": self.nombre,
        "notas": [nota.to_dict() for nota in self.notas]
    }  




