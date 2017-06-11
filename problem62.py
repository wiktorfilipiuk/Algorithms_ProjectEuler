"""
@Author: Wiktor Filipiuk <wiktor.filipiuk@gmail.com>
@ProblemName: Cubic permutations
-----------------------------------------------------------------------
@Description:

The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest
cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

"""

def findCube(x):
	return(x**3)

def solve(permCubeNumber):
	permCubeFound = 0
	i = 0
	charCubes = []
	result = 0
	candidates = []
	while permCubeFound < permCubeNumber:
		
		#-- generate permutation candidate
		cube = findCube(i)
		tmp = [character for character in str(cube)]
		tmp.sort()
		charCubes.append(tmp)
		permCubeFound = charCubes.count(tmp)
		i = i + 1
		
		if i % 100 == 0:
			print("i: {0}, tmp: {1}".format(i, tmp))
			print("permCubeFound: {0}".format(permCubeFound))
		
	candidates = [i for i, x in enumerate(charCubes) if x == tmp]
	result = findCube(min(candidates))
	return(result)

a = solve(5)
print(a)






