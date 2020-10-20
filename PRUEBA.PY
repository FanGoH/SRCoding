# array = []

# for i in range(0, 5):
#     array[i] = input()

# sumaMinima = 2000000
# sumaMaxima = 0

# for valor in range(0, len(array)):
#     sumaActual = 0
    
#     for valorArevisar in range(0, len(array)):
#         if(valorArevisar == valor):
#             continue
#         sumaActual = sumaActual + array[valorArevisar]

#     if (sumaActual < sumaMinima):
#         sumaMinima = sumaActual

#     if (sumaActual > sumaMaxima):
#         sumaMaxima = sumaActual


# print(f"{sumaMinima} {sumaMaxima}")

n=17
for i in range(1, (2**2016)+1):
    n*=17

    if(((n)-1)%(2**2016) == 0):
        print(i)    


