"""
@Author: Wiktor Filipiuk <wiktor.filipiuk@gmail.com>
@ProblemName: Distinct primes factors
-----------------------------------------------------------------------
@Description:
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each.
What is the first of these numbers?

"""

def findFactors(num):
    primes = []
    i = 2
    while num > 1:
        if num % i == 0:
            primes.append(i)
            num = num/i
        else:
            i += 1
    return(list(set(primes)))

def solve(n):
    num = 2
    lista = []
    while len(lista) < n:
        if num %1000 == 0:
            print(num)
        lista = []
        for i in range(n):
            if len(findFactors(num + i)) == n:
                lista.append(num+i)
            else:
                break
        num += 1
    return(lista)

print(solve(4))