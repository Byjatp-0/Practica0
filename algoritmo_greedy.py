mapa = [
    ['S','.','.','.','.','#','.'],
    ['#','#','#','.','.','.','.'],
    ['#','#','.','.','#','#','.'],
    ['#','#','.','#','#','.','.'],
    ['#','#','.','.','.','E','#']
]
def determinar_ubicacion():
    for i in range (0,numero_de_filas_de_mapa):
        for j in range (0,numero_de_columnas_de_mapa): 
            if mapa[i][j] == 'S':                
                ubicacion = "posición actual = ["+str(i)+"]"+"["+str(j)+"]"                
                return i,j,ubicacion

def movimiento_principio(i,j):
    if mapa[i+1][j] == '.':
        ubicacion = "posición actual = ["+str(i)+"]"+"["+str(j)+"]" #mover derecha
        direccion = 'E'
        i = i + 1
    elif mapa[i][j+1] == '.':
        ubicacion = "posición actual = ["+str(i)+"]"+"["+str(j)+"]" #mover abajo
        direccion = 'S'
        j = j + 1
    return i, j, direccion

def movimiento_izquierda(i,j):
    

    if mapa[i][j+1] == '.':
        ubicacion = "posición actual = ["+str(i)+"]"+"["+str(j)+"]" #mover abajo
        direccion = 'S'
        j = j + 1
    elif mapa[i-1][j] == '.':
        ubicacion = "posición actual = ["+str(i)+"]"+"["+str(j)+"]" #mover izquierda
        direccion = 'W'
        i = i - 1
    elif mapa[i][j-1] == '.':
        ubicacion = "posicion actual = ["+str(i)+"]"+"["+str(j)+"]" #mover arriba
        direccion = 'N'
        j = j - 1
    contador = contador + 1
    return i, j, direccion

def movimiento_derecha(i,j):
    if mapa[i+1][j] == '.':
        ubicacion = "posición actual = ["+str(i)+"]"+"["+str(j)+"]" #mover derecha
        direccion = 'E'
        i = i + 1
    elif mapa[i][j+1] == '.':
        ubicacion = "posición actual = ["+str(i)+"]"+"["+str(j)+"]" #mover abajo
        direccion = 'S'
        j = j + 1
    elif mapa[i][j-1] == '.':
        ubicacion = "posicion actual = ["+str(i)+"]"+"["+str(j)+"]" #mover arriba
        direccion = 'N'
        j = j - 1
    contador = contador + 1
    return i, j, direccion

def movimiento_abajo(i,j):
    if mapa[i+1][j] == '.':
        ubicacion = "posición actual = ["+str(i)+"]"+"["+str(j)+"]" #mover derecha
        direccion = 'E'
        i = i + 1
    elif mapa[i][j+1] == '.':
        ubicacion = "posición actual = ["+str(i)+"]"+"["+str(j)+"]" #mover abajo
        direccion = 'S'
        j = j + 1
    elif mapa[i-1][j] == '.':
        ubicacion = "posicion actual = ["+str(i)+"]"+"["+str(j)+"]" #mover izquierda
        direccion = 'W'
        i = i - 1
    contador = contador + 1
    return i, j, direccion
    
def movimiento_arriba(i,j):
    if mapa[i+1][j] == '.':
        ubicacion = "posición actual = ["+str(i)+"]"+"["+str(j)+"]" #mover derecha
        direccion = 'E'
        i = i + 1
    elif mapa[i][j-1] == '.':
        ubicacion = "posición actual = ["+str(i)+"]"+"["+str(j)+"]" #mover arriba
        direccion = 'N'
        j = j - 1
    elif mapa[i-1][j] == '.':
        ubicacion = "posicion actual = ["+str(i)+"]"+"["+str(j)+"]" #mover izquierda
        direccion = 'W'
        i = i - 1
    contador = contador + 1
    return i, j, direccion

def main():
    i,j,ubicacion = determinar_ubicacion()
    i,j,direccion = movimiento_principio(i,j)
    if direccion == 'E':
        i,j,direccion = movimiento_derecha(i,j)
    elif direccion == 'S':
        i,j,direccion = movimiento_abajo(i,j)
    



