#!/usr/bin/env python3

# EJERCICIO 3

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
nota = []
for asignatura in asignaturas:
    nota = input("¿Qué nota has sacado en " + asignatura + "?")
    nota.append(nota)
for i in range(len(asignaturas)):
    print("En " + asignaturas[i] + " has sacado " + nota[i])