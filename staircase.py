n=int(input())

for i in range(0, n):
    string = ""
    for j in range(0, n):
        if j < n-(i+1):
            caracter = " "
        else:
            caracter = "#"
        string += caracter
    print(string)

