"""
@Author: Wiktor Filipiuk <wiktor.filipiuk@gmail.com>
@ProblemName: 10001st prime
-----------------------------------------------------------------------
@Description:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

def primes(x):
    myList = []
    i=2
    while len(myList) != x:
        isPrime = True
        counter = 0

        while isPrime == True and counter != len(myList):
            if i % myList[counter] == 0:
                isPrime = False
            counter = counter + 1

        if isPrime == True:
            myList.append(i)

        i = i+1

    return myList

print primes(10001)
