#!/usr/bin/env python3

# EJERCICIO 2

storedPasswd = "abcd*1234"

passwd = input("Introduce tu contraseña:")
if (storedPasswd == passwd.strip()) :
    print("La contraseña coincide")
else : 
    print("La contraseña no coincide")
