"""
@Author: Wiktor Filipiuk <wiktor.filipiuk@gmail.com>
@ProblemName: Digit factorial chains
-------------------------------------------------------------------------
@Description:

The number 145 is well known for the property that the sum of the factorial of its
digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that
link back to 169; it turns out that there are only three such loops that exist:

169 -> 363601 -> 1454 -> 169
871 -> 45361 -> 871
872 -> 45362 -> 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop.
For example,

69 -> 363600 -> 1454 -> 169 -> 363601 (-> 1454)
78 -> 45360 -> 871 -> 45361 (-> 871)
540 -> 145 (-> 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating
chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

"""

from numpy import prod

def factorial(x):
	return prod([x for x in range(1,x+1)])

def sumOfDigitFactorial(x):
	digits = str(x)
	digitList = [int(i) for i in digits]
	return int(sum([factorial(i) for i in digitList]))

def findChain(x):
	chain = []
	tmp = int(x)
	while not (tmp in chain):
		chain.append(tmp)
		tmp = int(sumOfDigitFactorial(tmp))
	return(len(chain))

def solve():
	result = 0
	for i in range(1, 1000000):
		if (i % 1000) == 0:
			print("{0}%".format(i/1e5))
		if findChain(i) == 60:
			result = result + 1
	return(result)
		

print(solve())




































