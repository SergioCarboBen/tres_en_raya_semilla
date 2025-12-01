def comprobar_ganador(x, y, tablero):

    # ¿Qué casilla tenemos que comprobar?
    jugador = tablero[x][y]
    print("Voy a comprobar ", jugador, " en ", x, ",", y)

    ##########################################
    # Miramos hacia la izquierda y derecha
    if tablero[0][y] == tablero[1][y] and tablero[1][y] == tablero[2][y]:
        victoria_lateral = True
    
    if victoria_lateral:
        return True
    ##########################################
    # Miramos hacia abajo
    if tablero[x][0] == tablero[x][1] and tablero[x][1] == tablero[x][2]:
        victoria_columna = True

    if victoria_columna:
        return True
    ##########################################
    # Diagonal
    victoria_diagonal = True
        

    return False


def mostrar_tablero(tablero):
    for linea in tablero:
        print(linea)

# X --> 1
# O --> -1
# - --> 0
def convertir_tablero(tablero):
    nuevo_tablero = []
    for fila in tablero:
        fila_traducida = []
        fila_separada = tuple(fila)
        for casilla in fila_separada:
            if casilla == 'X': 
                fila_traducida.append(1)
            elif casilla == 'O':
                fila_traducida.append(-1)
            else:
                fila_traducida.append(0)
        nuevo_tablero.append(fila_traducida)

    ##########################################
    #TODO: Convertirlo a una lista de listas
    # ej: [[1,1,0], [1,-1,-1], [0, 0, 0]]

    return nuevo_tablero
