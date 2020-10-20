entrada = "12:40:41PM"

letra = entrada[len(entrada)-2]
numeros = entrada.split(":")

hora = int(numeros[0])
# minutos = (numeros[1])
# segundos = (numeros[2][0:2])
adicional = f"{numeros[1]}:{numeros[2][0:2]}"

if letra == "A":
    if(hora == 12):
        hora = 0

else:
    hora += 12
    if(hora == 24):
        hora = 12

if(hora < 10):
    hora = "0" + str(hora)

print(f"{hora}:{adicional}")

# salida = 00:40:41