def findMult(a,b,limit):
    myList = []
    for element in range(2,limit):
        #print(element)
        if element%3 == 0 or element%5 == 0:
            myList.append(element)
    return sum(myList)

x = findMult(3,5,1000)
print(x)
