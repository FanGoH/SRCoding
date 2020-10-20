arr = [4, 1, 4, 2]

maximo = 0
maximoCount = 0

for i in range(0, len(arr)):
    if(arr[i] == maximo ):
        maximoCount += 1
    elif(arr[i] > maximo):
        maximo = arr[i]
        maximoCount = 1

print(maximoCount)