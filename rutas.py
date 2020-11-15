def encontrar_ruta(C):
    matriz = testMatriz(C, 0, 0)
    if matriz == []:
        return []
    else: 
        for i in range(0, len(matriz)):
            for j in range (0, len(matriz[0])):
                if matriz[i][j] == 'b':
                    matriz[i][j] = 1
                else:
                    matriz[i][j] = 0
    return matriz
