import math

l = int(input("enter lower bound : "))
u = int(input("enter upper bound : "))

def isPrime(n):
    if n <= 1:
        return False
    for i in range (2, int(math.sqrt(n)) + 1):
        if (n%i == 0):
            return False
        
    return True

for i in range(l, u + 1):
    if (isPrime(i)):
        print(i)
