import math
import random
import numpy as np
class FourthSem:
    def __init__(self, r, l1, l2, l3):
        self.r = r
        self.t1 = l1
        self.t2 = l2
        self.t3 = l3
        
    def avg(self, test):
        
        avg = sum(test)/len(test)
        print(f"average is : {avg}")
        
r = [i + 1 for i in range(20)]
t1 = [random.randint(0, 100) for i in range(20)]
t2 = [random.randint(0, 100) for i in range(20)]
t3 = [random.randint(0, 100) for i in range(20)]


fs = FourthSem(r, t1, t2, t3)

fs.avg(fs.t1)
fs.avg(fs.t2)
fs.avg(fs.t3)
        
fs.t1.sort()
fs.t2.sort()
fs.t3.sort()

print("top 5 of test 1 : ")
print(fs.t1[0:5])
print("top 5 of test 2 : ")
print(fs.t2[0:5])
print("top 5 of test 3 : ")
print(fs.t3[0:5])

print("bottom 3 of test 1 : ")
print(fs.t1[-6:-1])
print("bottom 3 of test 2 : ")
print(fs.t2[-6:-1])
print("bottom 3 of test 3 : ")
print(fs.t3[-6:-1])