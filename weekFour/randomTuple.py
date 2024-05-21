import random

k = int(input("enter number : "))

randList = [random.randint(0, 100) for i in range(10)]

t = tuple(randList)

l = list(t)
    
l.sort()

answerList = [(l[i], l[-(i + 1)]) for i in range (k)]

answerTuple = tuple(answerList)

print(answerTuple)

