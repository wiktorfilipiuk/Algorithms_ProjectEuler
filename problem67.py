"""
@Author: Wiktor Filipiuk <wiktor.filipiuk@gmail.com>
@ProblemName: Maximum path sum II
-----------------------------------------------------------------------
@Description:

By starting at the top of the triangle below and moving to adjacent 
numbers on the row below, the maximum total from top to bottom is 23.

    "3"
  "7" 4
  2 "4" 6
 8 5 "9" 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in inputFiles/triangle.txt, 
a 15K text file containing a triangle with one-hundred rows.

"""

def loadData(path):
	with open(path, 'r') as f:
		array = []
		for line in f:
			array.append([int(x) for x in line.split()])
	return(array)

def reduceLayer(layer1, layer2):
	outputLayer = [x for x in layer1]
	for i in range(len(outputLayer)):
		outputLayer[i] = outputLayer[i] + max(layer2[i], layer2[i+1])
	return(outputLayer)
	

def solve():
	triangle = loadData("inputFiles/triangle.txt")
	nLevels = len(triangle)
	for level in reversed(range(nLevels-1)):
		reducedLayer = reduceLayer(triangle[level], triangle[level+1])
		triangle[level] = reducedLayer
		#print(reducedLayer)

solve()
