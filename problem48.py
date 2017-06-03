"""
@Author: Wiktor Filipiuk <wiktor.filipiuk@gmail.com>
@ProblemName: Self powers
-----------------------------------------------------------------------
@Description:
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

"""

def getNum(n):
    result = 0
    for i in range(1,n+1):
        result += i**i
    return(result)

def solve():
    number = getNum(1000)
    num = str(number)
    return(num[-10:])

print(solve())