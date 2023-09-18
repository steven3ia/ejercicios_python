#!/usr/bin/env python3

# EJERCICIO 7

peso = input("¿Cual es peso (kg)?:")
estatura = input("¿Cual es tu estatura?:")

imc = round(float(peso)/float(estatura)**2,2)

print("Tu masa de indice corporal es:",imc)