
#list operations : 
l = []
l.insert(0, 1)
l.insert(1, 2)
print(l)
l.remove(1)
print(l)
l.append(3)
print(l)
print(len(l))
print(l.pop())
print(l)
l.clear()
print(l)

#tuple operations : 
tup = (1, 2, 3)
# tup.insert(4)
# tup.append(4)
# tup.remove(2)
# tup.pop()
print(len(tup))
print(tup)

#dictionary operations:

d = {}
d["item1"] = 1
d["item2"] = 2
d["item3"] = 3

# d.append(3)
# d.remove("item1")
# d.insert(("item4", 4))
print(len(d))

for i in d.keys():
    print("item is here : ", d[i])

print(d)