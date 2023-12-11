import random

tablero = [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]

tablero_num = [[7, 8, 9],
               [4, 5, 6],
               [1, 2, 3]]

tablero_valor = ["X","O"]

def jugadorInicial():
    jugador1 = random.randint(0, 1)
    jugador1_valor = random.choice(tablero_valor)
    jugador2 = 1 if jugador1 == 0 else 0
    jugador2_valor = tablero_valor[1] if jugador1_valor == tablero_valor[0] else tablero_valor[0]
    return jugador1, jugador1_valor, jugador2, jugador2_valor

def imprimirTablero():
    print("+----+----+----+")
    print("| " + tablero[0][0] + "  | " + tablero[0][1] + "  | " + tablero[0][2] + "  |")
    print("+----+----+----+")
    print("| " + tablero[1][0] + "  | " + tablero[1][1] + "  | " + tablero[1][2] + "  |")
    print("+----+----+----+")
    print("| " + tablero[2][0] + "  | " + tablero[2][1] + "  | " + tablero[2][2] + "  |")
    print("+----+----+----+")

def buscar_pos(item):
    for x in range(len(tablero_num)):
        for y in range(len(tablero_num[x])):
            if tablero_num[x][y] == item:
                return x, y

def verificar_ganador():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] != " ":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != " ":
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
        return True

    return False


def iniciar_juego():
    jugador1, jugador1_valor, jugador2, jugador2_valor = jugadorInicial()
    
    print("#######################")
    print("##### TIC TAC TOE #####")
    print("#######################")
    

    imprimirTablero()
    
    print("Empieza el jugador" , jugador1 + 1)

    for i in range(9):
        item = int(input("Introduce el movimiento: "))
        x, y = buscar_pos(item)
        if i % 2 == jugador1:
            if tablero[x][y] == " ":
                tablero[x][y] = jugador1_valor
            else:
                print("¡Casilla ocupada! Introduce otra posición: ")
                i -= 1 
        else:
            if tablero[x][y] == " ":
                tablero[x][y] = jugador2_valor
            else:
                print("¡Casilla ocupada! Introduce otra posición: ")
                i -= 1 

        imprimirTablero()   
         
        if verificar_ganador():
            print(f"¡El jugador x ha ganado!")
            break

iniciar_juego()