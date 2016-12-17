from itertools import permutations

def getPandigitalNumbers():
    perms = [''.join(p) for p in permutations('0123456789')]
    return perms

def isDivisible(n):
    primes = [2,3,5,7,11,13,17]
    for i in range(7):
        number = int(n[i+1:i+4])
        if number%primes[i] != 0:
            return False
    return True

def solve():
    nums = getPandigitalNumbers()
    suma = 0
    i=0
    for item in nums:
        if i %10000 == 0:
            print i
        i += 1
        if isDivisible(item):
            suma += int(item)
    return suma

print solve()
