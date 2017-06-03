"""
@Author: Wiktor Filipiuk <wiktor.filipiuk@gmail.com>
@ProblemName: Consecutive prime sum
-----------------------------------------------------------------------
@Description:
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred. The longest sum of consecutive primes below one-thousand that
adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

"""
from math import ceil

def isPrime(n):
    for i in range(2, ceil(n/2)):
        if n%i == 0:
            return(False)
    return(True)

def getPrimesBelow(n):
    i = 2
    primes = []
    isPrime = True
    for i in range(2,n):
        isPrime = True
        for prime in primes:
            if i%prime == 0:
                isPrime = False
        if isPrime:
            primes.append(i)
    return(primes)

def solve(n):
    primes = getPrimesBelow(n)
    maxLen = 0
    result = []
    for i in range(len(primes)):
        if i%10 == 0:
            print(i)
        for j in range(len(primes)):
            tmp = sum(primes[i:(len(primes)-j)])
            tmpLen = - i + len(primes) - j
            if isPrime(tmp):
                if tmpLen >= maxLen:
                    maxLen = tmpLen
                    result.append(tmp)
    return(result)

print(solve(10000))