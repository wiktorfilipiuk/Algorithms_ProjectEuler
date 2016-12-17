def isPrime(n):
    for i in range(2,n/2):
        if n%i == 0:
            return False
            
    return True

def solve():
    primes = []
    result = []
    for i in range(1000,10000):
        if isPrime(i):
            primes.append(i)
    print "Generating primes finished!"

    for i in range(len(primes)):
        for j in range(i+1,len(primes)):
            if sorted(str(primes[i])) == sorted(str(primes[j])):
                tmp = primes[j] + (primes[j] - primes[i])
                if isPrime(tmp):
                    if sorted(str(primes[i])) == sorted(str(tmp)):
                        result.append([primes[i], primes[j], tmp])
    return result

print solve()

        


