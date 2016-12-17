def findTriplet():
    a = 1
    b = 1
    c = 1
    lista = []
    for i in range(1,1000):
        for j in range(1,1000):
            a = i
            b = j
            c = 1000 - a - b
            if(((a**2) + (b**2))  == (c**2)):
                lista.append([a,b,c])
    return lista
            

print findTriplet()
            
