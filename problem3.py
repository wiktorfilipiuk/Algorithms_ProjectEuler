# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def znajdzDzielniki(x):
    result = []
    n = 2
    tmp = x
    while tmp != 1:
        if tmp%n == 0:
            result.append(tmp)
            tmp = tmp/n
            result.append(tmp)
        else:
            n = n + 1
    return result


def znajdzMaxPrime(x):
    lista = znajdzDzielniki(x)
    return [element for element in lista if len(znajdzDzielniki(element)) == 2]

a =  znajdzMaxPrime(600851475143)
                      



