# 2520 is the smallest number that can be divided by each
# of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20? 
import operator

def findDivision(x):
    result = []
    n = 2
    while x != 1:
        if x%n == 0:
            result.append(n)
            x = x/n
        else:
            n = n + 1
    return result

def findFactors(x):
    lista = []
    for i in range(2,x+1):
        subLista = findDivision(i)
        for j in reversed(range(len(subLista))):
            if reduce(operator.mul,lista,1)%reduce(operator.mul,subLista,1) == 0:
                print(i)
            else:
                lista.append(subLista[j])
    return reduce(operator.mul,lista,1)
                

        
print str(findFactors(20))
