"""
@Author: Wiktor Filipiuk <wiktor.filipiuk@gmail.com>
@ProblemName: Sum square difference
-----------------------------------------------------------------------
@Description:
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.

"""

def sumOfSquares(x):
    lista = range(1,x+1)
    return sum([x**2 for x in lista])

def squareOfSum(x):
    return (sum(range(1,x+1)))**2

def problem(x):
    return (squareOfSum(x) - sumOfSquares(x))

print(problem(100))
