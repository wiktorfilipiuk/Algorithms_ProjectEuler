def findPrimes(x):
    lista = []
    for i in range(2,x):
        isPrime = True
        counter = 0
        while isPrime == True and counter != len(lista):
            if i%lista[counter] == 0:
                isPrime = False
            counter = counter + 1
        if isPrime == True:
            lista.append(i)
    return sum(lista)


print findPrimes(2000000)
