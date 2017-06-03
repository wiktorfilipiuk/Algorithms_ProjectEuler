"""
@Author: Wiktor Filipiuk <wiktor.filipiuk@gmail.com>
@ProblemName: Powerful digit sum
-----------------------------------------------------------------------
@Description:
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.

Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

"""

def sumOfDigits(n):
	s = str(n)
	result = 0
	for element in s:
		result = result + int(element)
	return(result)
	
a_range = range(1,101)
b_range = range(1,101)

maxSum = 0
maxA = 0
maxB = 0

for a in a_range:
	print("{0}% Progress".format(str(a)))
	for b in b_range:
		ab = sumOfDigits(a**b)
		if ab > maxSum:
			maxSum = ab
			maxA = a
			maxB = b

print(maxSum)
print(maxA)
print(maxB)
print(maxA**maxB)
print(sumOfDigits(maxA**maxB))