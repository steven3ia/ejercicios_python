#!/usr/bin/env python3
import json
import os
from model.alumno import Alumno
# Comprobamos si existen los archivos JSON para manipular la informacions
# En caso de no existir creamos los archivos en el mismo directorio
def crear_archivos_json():
    if not os.path.exists("data/alumnos.json"):
        with open("data/alumnos.json", 'w') as file:
            json.dump([], file)
        print(f"Se ha creado el archivo data/alumnos.json")

    if not os.path.exists("data/asignaturas.json"):
        with open("data/asignaturas.json", 'w') as file:
            json.dump([], file)
        print(f"Se ha creado el archivo asignaturas.json")

    if not os.path.exists("data/notas.json"):
        with open("data/notas.json", 'w') as file:
            json.dump([], file)
        print(f"Se ha creado el archivo notas.json")

# Llama a la función para crear los archivos JSON si no existen
crear_archivos_json()

# Definimos las funciones de las diferentes opciones
def crear_alumno():
    # Recogemos los datos del alumno
    print("------------Crear un nuevo alumno------------")
    dni = input("DNI: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    fecha_nacimiento = input("Fecha de nacimiento: ")
    # Creamos una nueva instancia del Alumno
    nuevo_alumno = Alumno(dni, nombre, apellido, edad, fecha_nacimiento)
    # Creamos un array vacio de alumnos
    alumnos = [] 
    # Comprobamos que el archivo existe y cargamos los alumnos que ya habian
    with open("data/alumnos.json", 'r') as file:
        alumnos = json.load(file)
    # Guardamos el nuevo alumno en un diccionario
    alumnos.append(nuevo_alumno.to_dict())
    # Escribimos los nuevos alumnos en el fichero
    with open("data/alumnos.json", 'w') as file:
        json.dump(nuevo_alumno, file, indent=4)
    print("------------Nuevo alumno creado------------")

def buscar_alumno():
    dni_a_buscar = input("Dni del alumno a buscar:")
    # Creamos un array vacio de alumnos
    alumnos = []
    # Leemos el fichero con al informacion de todos los alumnos
    with open("data/alumnos.json", 'r') as file:
            alumnos = json.load(file)
    # Miramos si el dni existe entre todos los alumnos
    for alumno in alumnos:
        if alumno["dni"] == dni_a_buscar:
            alumno_encontrado = alumno
            break
    # Comprobamos si se ha encontrado un alumno con ese dni
    if alumno_encontrado:
        print("-----Se ha encontrado el alumno con el dni:", dni_a_buscar, "-----")
        print("Nombre: ", alumno_encontrado["nombre"])
        print("Apellido: ", alumno_encontrado["apellido"])
        print("Edad: ", alumno_encontrado["edad"])
        print("Fecha nacimiento: ", alumno_encontrado["fecha_nac"])
        print("-------------------------------------")
    else:
        print("-----No se ha encontrado el alumno con el dni:", dni_a_buscar, "-----")

def mostrar_todos_alumnos():
    print("Lista de todos los alumnos:")
    # Creamos un array vacio de alumnos
    alumnos = [] 
    # Leemos todos los datos de los alumnos del fichero
    with open("data/alumnos.json", 'r') as file:
        alumnos = json.load(file)
    # Bucle para imprimir todos los alumnos
    for alumno in alumnos:
        print("-----ALUMNO CON DNI:", alumno["dni"], "-----")
        print("Nombre: ", alumno["nombre"])
        print("Apellido: ", alumno["apellido"])
        print("Edad: ", alumno["edad"])
        print("Fecha nacimiento: ", alumno["fecha_nac"])
        print("-------------------------------------")

def actualizar_alumno():
    dni_a_buscar = input("Dni del alumno a buscar:")
    # Creamos un array vacio de alumnos
    alumnos = []
    # Leemos el fichero con al informacion de todos los alumnos
    with open("data/data/alumnos.json", 'r') as file:
            alumnos = json.load(file)
    # Miramos si el dni existe entre todos los alumnos
    for alumno in alumnos:
        if alumno["dni"] == dni_a_buscar:
            alumno_encontrado = alumno
            break
    # Comprobamos si se ha encontrado un alumno con ese dni
    if alumno_encontrado:
        print("-----Se ha encontrado el alumno con el dni:", dni_a_buscar, "-----")
        # Recogemos los nuevos datos para actualizar el alumno
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = int(input("Edad: "))
        fecha_nacimiento = input("Fecha de nacimiento: ")
        # Creamos una nueva instancia del Alumno
        nuevo_alumno = Alumno(dni_a_buscar, nombre, apellido, edad, fecha_nacimiento)
        # Creamos un array vacio de alumnos
        alumnos = [] 
        # Comprobamos que el archivo existe y cargamos los alumnos que ya habian
        with open("data/alumnos.json", 'r') as file:
            alumnos = json.load(file)
        # Guardamos el nuevo alumno en un diccionario
        alumnos.append(nuevo_alumno.to_dict())
        # Escribimos los nuevos alumnos en el fichero
        with open("data/alumnos.json", 'w') as file:
            json.dump(alumnos, file, indent=4)
        print("-----------Alumno acutalizado---------------")
    else:
        print("-----No se ha encontrado el alumno con el dni:", dni_a_buscar, "-----")

def eliminar_alumno():
    # Recogemos el dni del alumno a eliminar
    print("-----Eliminar alumno-----")
    dni_a_eliminar = input("Ingrese el DNI del alumno que desea eliminar: ")
    # Creamos un array vacio de alumnos
    alumnos = []
    alumno_encontrado = None 
    # Leemos el fichero con al informacion de todos los alumnos
    with open("data/alumnos.json", 'r') as file:
            alumnos = json.load(file)
    # Miramos si el dni existe entre todos los alumnos
    for alumno in alumnos:
        if alumno["dni"] == dni_a_eliminar:
            alumno_encontrado = alumno
            break
    # Comprobamos si se ha encontrado un alumno con ese dni
    if alumno_encontrado:
        alumnos.remove(alumno_encontrado)
        # Actualizamos la informacion con los alumnos actuales
        with open("data/alumnos.json", 'w') as file:
            json.dump(alumnos, file, indent=4)
        print("-----Se ha eliminado el alumno con el dni:", dni_a_eliminar, "-----")
    else:
        print("-----No se ha eliminado el alumno con el dni:", dni_a_eliminar, "-----")

def salir_del_programa():
    print("Hasta la proxima")
    exit()

# Hacemos un diccionario para guardar las posibles opciones
opciones = {
    "1": crear_alumno,
    "2": buscar_alumno,
    "3": mostrar_todos_alumnos,
    "4": actualizar_alumno,
    "5": eliminar_alumno,
    "0": salir_del_programa
}

while True:
    # Menu a mostra en la linea de comnados
    print("======  Menú ======")
    print("1. Crear alumno")
    print("2. Buscar alumno")
    print("3. Listar todos los alumnos")
    print("4. Actualizar alumno")
    print("5. Eliminar alumno")
    print("0. Salir")

    # Recogemos la opcion que ha escrito el usuario
    opcion = input("Selecciona una opcion: ").strip() 

    if opcion in opciones:
        # Llamamos a la funcion dependiendo de la opcion escogida
        opciones[opcion]()
    else:
        print("Opcion no valida. Vuelva introducir una opcion")
    



