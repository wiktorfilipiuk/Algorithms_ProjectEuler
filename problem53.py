"""
@Author: Wiktor Filipiuk <wiktor.filipiuk@gmail.com>
@ProblemName: Combinatoric selections
-----------------------------------------------------------------------
@Description:
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5_C_3 = 10.

In general,
n_C_r = n! / r!(n−r)!
	,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23_C_10 = 1144066.

How many, not necessarily distinct, values of  n_C_r, for 1 ≤ n ≤ 100, are greater than one-million?

"""

from functools import reduce

def factorial(n):
	if n == 0 or n == 1:
		return(1)
	else:
		return(reduce(lambda x, y: x*y, range(1,n+1)))

def ncr(n, r):
	return(factorial(n)/(factorial(r)*factorial(n-r)))


def find():
	counter = 0
	for i in range(1,101):
		for j in range(1,i):
			if ncr(i,j) > 1000000:
				counter = counter + 1
	return(counter)

print(find())