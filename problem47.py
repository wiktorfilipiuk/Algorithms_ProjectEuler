def findFactors(num):
    primes = []
    i = 2
    while num > 1:
        if num % i == 0:
            primes.append(i)
            num = num/i
        else:
            i += 1
    return list(set(primes))

def solve(n):
    num = 2
    lista = []
    while len(lista) < n:
        if num %1000 == 0:
            print num
        lista = []
        for i in range(n):
            if len(findFactors(num + i)) == n:
                lista.append(num+i)
            else:
                break
        num += 1
    return lista

print solve(4)


