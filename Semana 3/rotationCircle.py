def rotateArray(array, rotNum, queries):
    # HICIMOS ROTACIONES A MANITA
    # resultadoQueries = []
    # for _ in range(0, rotNum):
    #     temp = array[0]
    #     for i in range(0, len(array)):
    #         array[(i+1)%len(array)], temp = temp, array[(i+1)%len(array)] 

    # for query in queries:
    #     resultadoQueries.append(array[query])
    # return resultadoQueries

    # HICIMOS LAS ROTACIONES AL TRANCAZO
    # resultadoQueries = []
    # temp = array[0]
    # for i in range(0, len(array)):
    #     array[(i*rotNum+rotNum)%len(array)], temp = temp, array[(i*rotNum+rotNum)%len(array)] 

    # for query in queries:
    #     resultadoQueries.append(array[query])

    # return resultadoQueries

    # CONSULTAMOS LAS QUERIES
    resultadoQueries = []

    for query in queries:
        queryIndex = (query - rotNum) % len(array) 
        resultadoQueries.append(array[queryIndex])

    return resultadoQueries


arreglo = [1, 2, 3]

rotateArray(arreglo, 2, [0, 1, 2])

# print(arreglo)