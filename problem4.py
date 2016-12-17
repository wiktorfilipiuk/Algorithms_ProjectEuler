def checkIfPalindrome(value):
    iks = str(value)
    result = [i for i in range(1,len(iks)) if iks[i-1] != iks[-i] ]

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
