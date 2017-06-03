"""
@Author: Wiktor Filipiuk <wiktor.filipiuk@gmail.com>
@ProblemName: Largest palindrome product
-------------------------------------------------------------------------
@Description:
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def checkIfPalindrome(value):
    x = str(value)
    result = [i for i in range(1,len(x)) if x[i-1] != x[-i] ]

    if result == []:
        return True
    else:
        return False

def findPalindrome(digitNum):
    aMin = 10**(digitNum-1)
    bMin = 10**(digitNum-1)
    aMax = 10**digitNum
    bMax = 10**digitNum

    print str(aMin) + ', ' + str(bMin) + ', ' + str(aMax) + ', ' + str(bMax)    
    resultPalindrome = []
    
    for value1 in range(aMin, aMax):
        for value2 in range(bMin, bMax):
            if(checkIfPalindrome(value1 * value2)):
                resultPalindrome.append(value1*value2)

    return max(resultPalindrome) 


print findPalindrome(3)
