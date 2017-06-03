"""
@Author: Wiktor Filipiuk <wiktor.filipiuk@gmail.com>
@ProblemName: Prime permutations
-----------------------------------------------------------------------
@Description:
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit 
numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting 
this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

"""
import math

def isPrime(n):
    for i in range(2,math.ceil(n/2)):
        if n%i == 0:
            return(False)
    return(True)

def solve():
    primes = []
    result = []
    for i in range(1000,10000):
        if isPrime(i):
            primes.append(i)
    print("Generating primes finished!")

    for i in range(len(primes)):
        for j in range(i+1,len(primes)):
            if sorted(str(primes[i])) == sorted(str(primes[j])):
                tmp = primes[j] + (primes[j] - primes[i])
                if isPrime(tmp):
                    if sorted(str(primes[i])) == sorted(str(tmp)):
                        result.append([primes[i], primes[j], tmp])
    return(result)

solution = solve()
print("Example result: {0}\nReal result: {1}".format("".join(str(x) for x in solution[0]), "".join(str(x) for x in solution[1])))