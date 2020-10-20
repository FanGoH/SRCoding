
def minMaxSum(array):
    sumaTotal = 0
    numeroMenor = 0
    numeroMayor = 0

    for valor in range(0, len(array)):
        sumaTotal = sumaTotal + array[valor]

        if (valor == 0):
            numeroMayor = array[valor]
            numeroMenor = array[valor]

        if(array[valor] < numeroMenor):
            numeroMenor = array[valor]

        if(array[valor] > numeroMayor):
            numeroMayor =  array[valor]

    print(f"{sumaTotal - numeroMayor} {sumaTotal - numeroMenor}")