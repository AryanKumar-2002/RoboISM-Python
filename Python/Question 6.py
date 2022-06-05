def isPrime (x):
    if x == 1: return False
    for i in range(2, int(x/2) + 1): 
        if (x%i == 0): return False
    else: return True

def primeNos (start, end):
    for i in range (start, end): 
        if isPrime(i): print (i)

#for testing
primeNos(1, 100)