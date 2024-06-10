
def crear_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" | " + " | ".join(fila) + " | ")    
        
def verificar_ganador(tablero,jugador):
    # Verificar filas, columnas y diagonales
    for i in range(3):
        #chequeo de filas
        if all([tablero[i][j] == jugador for j in range(3)]):
            return True
        #chequeo de columnas
        if all([tablero[j][i] == jugador for j in range(3)]):
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    return False

def tablero_lleno(tablero):
    return all([tablero[i][j] != " " for i in range(3) for j in range(3)])

def cambiar_jugador(actual):
    return "O" if actual == "X" else "X"

def hacer_movimiento(tablero, jugador, i, j):
    while True:
        file=int(input(f"{jugador} elige la fila 1,2 o 3: ")) - 1
        column=int(input(f"{jugador} elige la columna 1,2 o 3: ")) - 1
        if 0 <= file <= 3 and 0 <= column <= 3 and tablero[file][column] == " ":
            tablero[file][column] = jugador
            break
        else:
            print("Movimiento inválido. Intentalo de nuevo.")


def jugar():
    tablero = crear_tablero()
    jugador_actual = "X"
    while True:
        mostrar_tablero(tablero)
        hacer_movimiento(tablero, jugador_actual, 0, 0)
        if verificar_ganador(tablero, jugador_actual):
            mostrar_tablero(tablero)
            print(f"{jugador_actual} ha ganado!")
            break
        elif tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print("Empate!")
            break
        jugador_actual= cambiar_jugador(jugador_actual)
        
jugar()    