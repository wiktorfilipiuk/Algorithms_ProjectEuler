def sumOfDigits(n):
	s = str(n)
	result = 0
	for element in s:
		result = result + int(element)
	return result
	
a_range = range(1,101)
b_range = range(1,101)

maxSum = 0
maxA = 0
maxB = 0

for a in a_range:
	print str(a) + "% Progress"
	for b in b_range:
		ab = sumOfDigits(a**b)
		if ab > maxSum:
			maxSum = ab
			maxA = a
			maxB = b

print maxSum
print maxA
print maxB
print maxA**maxB
print sumOfDigits(maxA**maxB)