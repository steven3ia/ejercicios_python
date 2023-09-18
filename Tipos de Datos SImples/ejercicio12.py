#!/usr/bin/env python3

# EJERCICIO 12

barrasPan = 3.49
descuento = 0.6

numeroBarrasPan = int(input("Introduce el numero de barras de pan que no son del dia:"))

costeFinal = round((barrasPan * descuento) * numeroBarrasPan , 2)

print("Coste barras de pan:",barrasPan,"€")
print("Descuento pan no del dia:",(descuento * 100),"%")
print("Coste total por",numeroBarrasPan,"barras de pan es:",costeFinal,"€")