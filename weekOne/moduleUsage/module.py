import math

def triArea(a, b, c):
    s = (a + b + c)/2
    print("s is : ", s, " area is : ", math.sqrt(s*(s - a)*(s - b)*(s - c)))
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def circleArea(radius):
    return math.pi*radius*radius

def rectArea(l, b):
    return l*b