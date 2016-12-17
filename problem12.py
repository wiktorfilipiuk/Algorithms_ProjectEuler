def generateNumber(n):
    return sum(range(1,n+1))

def findDivisors(n):
    return set(reduce(list.__add__,([i,n//i] for i in range(1, int(n**0.5)+1) if n%i == 0)))

def findTriangle(t):
    length = 1
    i = 2
    number = 0
    while length <= t:
        number = generateNumber(i)
        divisors = findDivisors(number)
        length = len(divisors)
        i = i + 1
    return number

    
print findTriangle(500)




