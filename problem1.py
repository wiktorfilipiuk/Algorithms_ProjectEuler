"""
@Author: Wiktor Filipiuk <wiktor.filipiuk@gmail.com>
@ProblemName: Multiples of 3 and 5
-------------------------------------------------------------------------
@Description:
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def findMult(a,b,limit):
    myList = []
    for element in range(2,limit):
        #print(element)
        if element%3 == 0 or element%5 == 0:
            myList.append(element)
    return sum(myList)

x = findMult(3,5,1000)
print(x)
