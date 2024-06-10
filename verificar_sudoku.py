tablero_valido = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

tablero_invalido = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 9, 9]
]

def verificar_sudoku(tablero):
    #grupo valido
    def es_grupo_valido(grupo):
        numeros= [ num for num in grupo if num != 0 ]
        return len(set(numeros)) == len(numeros)
    
    for fila in tablero:
        if not es_grupo_valido(fila):
            return False
    for col in range(9):
        columna= [ fila[col] for fila in tablero ]
        if not es_grupo_valido(columna):
            return False
   
    for caja_fila in range(0,9,3):
        for caja_col in range(0,9,3):
            subcuadricula= [ tablero[f][c] for f in range(caja_fila,caja_fila+3) for c in range(caja_col,caja_col+3) ]
        if not es_grupo_valido(subcuadricula):
            return False
    
    return True

print(verificar_sudoku(tablero_valido))
print(verificar_sudoku(tablero_invalido))
            
            