def generateFibonacci(limit):
    lista = [1,2]
    while lista[-1] + lista[-2] <= limit:
        lista.append(lista[-1] + lista[-2])
    return lista        
    
def sumEvenFibonacci(lista):
    return sum([x for x in lista if x%2 == 0])

x = generateFibonacci(4000000)
print(sumEvenFibonacci(x))
