#!/usr/bin/env python3

# EJERCICIO 11

interes = 0.04

dineroDepositado = float(input("Introduce el dinero depositado en la cuenta de ahorros:"))

dineroTras1Ano = round(dineroDepositado * (interes + 1),2)
dineroTras2Ano = round(dineroTras1Ano * (interes + 1),2)
dineroTras3Ano = round(dineroTras2Ano * (interes + 1),2)

print("Cantidad de ahoroo tras el \n primer año:",dineroTras1Ano,"\n segundo año:",dineroTras2Ano,"\n tercer año:",dineroTras3Ano)