import math

cantidadDeFocos = 20

# interruptores = []

# for i in range(0, cantidadDeFocos):
#     interruptores.append(False)

# for k in range(1, cantidadDeFocos+1):
#     for i in range(0, cantidadDeFocos):
#         if((i+1) % k == 0):
#             interruptores[i] = not interruptores[i]

# focosPrendidos = 0

# for i in range(0, cantidadDeFocos):
#     if(interruptores[i]):
#         focosPrendidos += 1


# print(focosPrendidos)

print(math.floor(math.sqrt(cantidadDeFocos)))