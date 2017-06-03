"""
@Author: Wiktor Filipiuk <wiktor.filipiuk@gmail.com>
@ProblemName: Smallest multiple
-----------------------------------------------------------------------
@Description:
2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of 
the numbers from 1 to 20?

"""

import operator
from functools import reduce

def findDivision(x):
    result = []
    n = 2
    while x != 1:
        if x%n == 0:
            result.append(n)
            x = x/n
        else:
            n = n + 1
    return(result)

def findFactors(x):
    myList = []
    for i in range(2,x+1):
        mySubList = findDivision(i)
        for j in reversed(range(len(mySubList))):
            if reduce(operator.mul, myList, 1)%reduce(operator.mul, mySubList, 1) == 0:
                print(i)
            else:
                myList.append(mySubList[j])
    return(reduce(operator.mul, myList, 1))

print(str(findFactors(20)))