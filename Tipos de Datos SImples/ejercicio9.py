#!/usr/bin/env python3

# EJERCICIO 9

cantidadInvertir = float(input("Introduce la cantidad que va a invertir:"))
interesAnual = float(input("Introduce el interes anual:"))
numeroAnos = int(input("Introduce el numerto de años a invertir:"))

capital = round(cantidadInvertir * (interesAnual / 100 + 1) ** numeroAnos,2)

print("El capital que se obtendria en la inversion es:",capital)