def primes(x):
    lista = []
    i=2
    while len(lista) != x:
        isPrime = True
        counter = 0

        while isPrime == True and counter != len(lista):
            if i % lista[counter] == 0:
                isPrime = False
            counter = counter + 1

        if isPrime == True:
            lista.append(i)

        i = i+1

    return lista

print primes(10001)
