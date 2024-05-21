n = int(input("enter number of string : "))

l = []

for i in range(n):
    s = input(f"enter string {i + 1}")
    l.insert(i, (s, len(s)))
    
l.sort(key = lambda x : x[1])
    
print(l)