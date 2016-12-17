def factorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return reduce(lambda x, y: x*y, range(1,n+1))

def ncr(n, r):
	return factorial(n)/(factorial(r)*factorial(n-r))


def find():
	counter = 0
	for i in range(1,101):
		for j in range(1,i):
			if ncr(i,j) > 1000000:
				counter = counter + 1
	return counter

print find()