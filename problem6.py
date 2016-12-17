def sumOfSquares(x):
    lista = range(1,x+1)
    return sum([x**2 for x in lista])

def squareOfSum(x):
    return (sum(range(1,x+1)))**2

def problem(x):
    return (squareOfSum(x) - sumOfSquares(x))

print(problem(100))
