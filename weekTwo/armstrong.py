n = int(input("enter number : "))
sum = 0
m = n
count = 0

while (n):
    count += 1
    n //= 10

n = m

while (n):
    sum += (n%10)**count
    # print("n is : ", n)
    # print("sum is : ", sum)
    n = n//10  
# print(sum)
# print(m)
print("yes" if m == sum else "no")
