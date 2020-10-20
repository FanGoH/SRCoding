def saveThePrisioner(numPrison, numeroCaramelos, starting):
    # resultado = starting
    # for i in range(0, numeroCaramelos-1):
    
    #     resultado+=1

    #     if(resultado > numPrison):
    #         resultado = 1

    resultado = (starting + numeroCaramelos - 1) % numPrison 

    if resultado == 0:
        return numPrison
    return resultado

    # return resultado

print(saveThePrisioner(1000000000, 1000000000, 1000000000))