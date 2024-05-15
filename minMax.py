l = list(map(int, input("enter list : ").split()))

def displayMinMax(l):
    minimum = min(l)
    maximum = max(l)
    print(minimum, maximum)
    
def secondMax(l):
    currentMax = 0
    for i in range(1, len(l)):
        if (l[i] > currentMax and l[i] < max(l)):
            currentMax = l[i]
    print("second max is : ", currentMax)
    
displayMinMax(l)
secondMax(l)
