def sum(l):
    s = 0
    for i in range(len(l)):
        s += l[i]
    return s
def mul(l):
    m = 1;
    for i in range(len(l)):
        m *= l[i]
        print("multiplying with : ", l[i])
    return m

l = list(map(int, input("enter list : ").split()))
print("sum : ", sum(l))
print("mul : ", mul(l))
