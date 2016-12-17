def generateDiagonals(n):
	diagonals = []
	tmp = 1
	step = 0
	diagonals.append(tmp)
	for i in range(1,n):
		step = step + 2
		for j in range(4):
			tmp = tmp + step
			diagonals.append(tmp)
	return diagonals

import math

def genPrimes(n):
	result = []
	for num in range(2,n):
		if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
			result.append(num)
	return result
	
def isPrime2(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
	
def ratio(diagonals, primes):
	tmp = [x for x in diagonals if x in primes]
	print "len(tmp): " + str(len(tmp))
	print "len(diagonals): " + str(len(diagonals))
	return float(len(tmp)) / float(len(diagonals))

n = 1000
tmp = (n*2 -1)**2
print tmp
primes = genPrimes(tmp)
print primes
#diagonals = generateDiagonals(n)
#print diagonals
#print ratio(diagonals,primes)
"""	
limit = 1
n = 10110
print("start")
diag = generateDiagonals(n)
print("finished diag")
limit = ratio(diag)
print("finished ratio")
print "Level: " + str(n) + " -- " + str(limit*100) + "%"

while limit > 0.1:
	limit = ratio(generateDiagonals(n))
	n = n + 1
	print "Level: " + str(n) + " -- " + str(limit*100) + "%"
print ratio
"""

	
	
	
	
	



