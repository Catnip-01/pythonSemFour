import math

a = int(input("enter a : "))
b = int(input("enter b : "))
c = int(input("enter c : "))

d = (b**2 - 4*a*c)

if (d < 0):
    print("roots are imaginary !")
    d = abs(d)
    root1 = (((-1)*b) + math.sqrt(d))/(2*a)
    root2 = (((-1)*b) - math.sqrt(d))/(2*a)
    
    print("roots are : ", root1, "i", root2, "i")
    
    
else:
    root1 = (((-1)*b) + math.sqrt(d))/(2*a)
    root2 = (((-1)*b) - math.sqrt(d))/(2*a)
    
    print("roots are : ", root1, root2)
