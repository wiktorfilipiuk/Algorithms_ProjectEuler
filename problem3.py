"""
@Author: Wiktor Filipiuk <wiktor.filipiuk@gmail.com>
@ProblemName: Largest prime factor
-------------------------------------------------------------------------
@Description:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def findDivisors(x):
    result = []
    n = 2
    tmp = x
    while tmp != 1:
        if tmp%n == 0:
            result.append(tmp)
            tmp = tmp/n
            result.append(tmp)
        else:
            n = n + 1
    return result


def findMaxPrime(x):
    myList = findDivisors(x)
    return [element for element in myList if len(findDivisors(element)) == 2]

a =  findMaxPrime(600851475143)
                      



