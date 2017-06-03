"""
@Author: Wiktor Filipiuk <wiktor.filipiuk@gmail.com>
@ProblemName: Permuted multiples
-----------------------------------------------------------------------
@Description:
It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.

"""

def isPermutation(a,b):
	a_str = str(a)
	b_str = str(b)
	if len(a_str) == len(b_str):
		if sorted(a_str) == sorted(b_str):
			return(True)
	return(False)

def find():
	found = False
	x1 = 0
	while found == False:
		x1 = x1 + 1
		if isPermutation(x1, x1*2):
			if isPermutation(x1, x1*3):
				if isPermutation(x1, x1*4):
					if isPermutation(x1, x1*5):
						if isPermutation(x1, x1*6):
							found = True
	return(x1)
	
print(find())
	
	