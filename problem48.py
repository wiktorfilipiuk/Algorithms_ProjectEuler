def getNum(n):
    result = 0
    for i in range(1,n+1):
        result += i**i
    return result

def solve():
    number = getNum(1000)
    num = str(number)
    return num[-10:]

print solve()

