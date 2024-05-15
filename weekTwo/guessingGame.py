guess = 11

count = 5

while (count):
    n = int(input("enter guess : "))
    print("good guess!" if n == guess else "try again!")
    count -= 1
print("game over!")
# for i in range(5):
#     n = int(input("enter guess : "))
#     print("good guess!" if n == guess else "try again!")
# print("game over!")