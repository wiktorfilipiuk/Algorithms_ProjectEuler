"""
@Author: Wiktor Filipiuk <wiktor.filipiuk@gmail.com>
@ProblemName: Powerful digit counts
-----------------------------------------------------------------------
@Description:
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

"""

import time

def nOfDigits(x):
	return(len(str(x)))

def solve():
	count = 0
	base = 1
	exponent = 1
	while True:
		if base == 10 and exponent = 1:
			break
		time.sleep(0.3)
		nDig = nOfDigits(base**exponent)
		print("{0}^{1} = {2}; nOfDigits = {3};  count = {4}".format(base, exponent, base**exponent, nDig, count))
		if exponent == nDig:
			count = count + 1
		
		
		if nDig > exponent:
			exponent = exponent + 1
			base = 1
			continue
		else:
			base = base + 1
#-- there's missing a STOP condition in this solution....
solve()