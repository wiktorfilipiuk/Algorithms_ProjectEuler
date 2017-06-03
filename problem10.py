"""
@Author: Wiktor Filipiuk <wiktor.filipiuk@gmail.com>
@ProblemName: Summation of primes
-----------------------------------------------------------------------
@Description:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

"""

def findPrimes(x):
    myList = []
    for i in range(2,x):
        if i%20000 == 0:
            print("Progress: {}%".format(i/20000))
        isPrime = True
        counter = 0
        while isPrime == True and counter != len(myList):
            if i%myList[counter] == 0:
                isPrime = False
            counter = counter + 1
        if isPrime == True:
            myList.append(i)
    return(sum(myList))

print(findPrimes(2000000))