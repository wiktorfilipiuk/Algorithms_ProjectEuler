"""
@Author: Wiktor Filipiuk <wiktor.filipiuk@gmail.com>
@ProblemName: Special Pythagorean triplet
-----------------------------------------------------------------------
@Description:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

def findTriplet():
    a = 1
    b = 1
    c = 1
    myList = []
    for i in range(1,1000):
        for j in range(1,1000):
            a = i
            b = j
            c = 1000 - a - b
            if(((a**2) + (b**2))  == (c**2)):
                myList.append([a,b,c])
    return myList
            

print findTriplet()