
def cantidadDeLikes(numDias):
    tabla = [[5, 2, 2]]
    
    for i in range(1, numDias):
        shared = tabla[i-1][1]*3
        liked = shared // 2
        acumulative = tabla[i-1][2] + liked

        fila = [shared, liked, acumulative]
        tabla.append(fila)
    
    return tabla[numDias-1][2]

    
print(cantidadDeLikes(5))