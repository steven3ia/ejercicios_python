#!/usr/bin/env python3
import json
import os
# Comprobamos si existen los archivos JSON para manipular la informacions
# En caso de no existir creamos los archivos en el mismo directorio
def crear_archivos_json():
    if not os.path.exists("alumnos.json"):
        with open("alumnos.json", 'w') as file:
            json.dump([], file)
        print(f"Se ha creado el archivo alumnos.json")

    if not os.path.exists("asignaturas.json"):
        with open("asignaturas.json", 'w') as file:
            json.dump([], file)
        print(f"Se ha creado el archivo asignaturas.json")

    if not os.path.exists("notas.json"):
        with open("notas.json", 'w') as file:
            json.dump([], file)
        print(f"Se ha creado el archivo notas.json")

# Llama a la función para crear los archivos JSON si no existen
crear_archivos_json()

# Definimos las funciones de las diferentes opciones
def crear_alumno():
    print("")
    pass

def mostrar_alumno():
    print("")
    pass

def mostrar_todos_alumnos():
    print("")
    pass

def actualizar_alumno():
    print("")
    pass

def eliminar_alumno():
    print("")
    pass

def salir_del_programa():
    print("Hasta la proxima")
    exit()

# Hacemos un diccionario para guardar las posibles opciones
opciones = {
    "1": crear_alumno,
    "2": mostrar_alumno,
    "3": mostrar_todos_alumnos,
    "4": actualizar_alumno,
    "5": eliminar_alumno,
    "6": salir_del_programa
}

while True:
    # Menu a mostra en la linea de comnados
    print("======  Menú ======")
    print("1. Crear alumno")
    print("2. Listar informacion del alumno")
    print("3. Listar todos los alumnos")
    print("4. Actualizar alumno")
    print("5. Eliminar alumno")
    print("6. Salir")

    # Recogemos la opcion que ha escrito el usuario
    opcion = input("Selecciona una opcion: ")

    if opcion in opciones:
        # Llamamos a la funcion dependiendo de la opcion escogida
        opciones[opcion]()
    else:
        print("Opcion no valida. Vuelva introducir una opcion")
    



