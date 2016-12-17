def solve(n):
    F1 = 1
    F2 = 1
    tmp = 0
    i = 2
    while len(str(F2)) < n:
        tmp = F1 + F2
        F1 = F2
        F2 = tmp
        print tmp
        i += 1
    return i

print solve(1000)
