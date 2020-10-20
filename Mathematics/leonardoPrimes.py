import math
primes = []
productOfPrimes = [2]


def leonardPrimes(n):

    maxValueToCheck = math.ceil(math.sqrt(n))

    maxCalculatedPrime = primes[len(primes) - 1] if (len(primes) != 0) else 2

    for possiblePrime in range(maxCalculatedPrime, maxValueToCheck+1):
        isPrime = True
        for prime in primes:
            if(possiblePrime % prime == 0):
                isPrime = False
                break

        if(isPrime):
            primes.append(possiblePrime)

    maxPrimes = 0

    maxProductOfPrimes = productOfPrimes[len(
        productOfPrimes) - 1] if (len(productOfPrimes) != 0) else 1

    for maxPrimes in range(0, len(primes)):
        if len(productOfPrimes) <= maxPrimes:
            productOfPrimes.append(
                productOfPrimes[len(productOfPrimes)-1]*primes[len(productOfPrimes)])

        if(productOfPrimes[maxPrimes] > n):
            break

    if(n == 1):
        return 0
    elif(maxPrimes == 0):
        return 1
    return maxPrimes


entradas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 30]
salida = []
expectedOut = [0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]

for entrada in entradas:
    salida.append(leonardPrimes(entrada))

print(salida)
print(expectedOut)
