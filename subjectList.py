l = [
    "Math",
    "MC IOT",
    "DAA",
    "DCN",
    "FAFL",
    "DAA lab",
    "DCN lab",
    "Python lab",
    "Data Analysis",
    "Angular JS"
    
]
for i in range(len(l)):
    print(l[i])
    
print("second and 5th elements are : ", l[1], "and : ", l[4])

print("first 4 elements : ", l[0:4])

print("last 4 elements : ", l[-4:])

if ("Python lab" in l):
    print("python lab is present")
else:
    print("python lab not present")
    
print("append function : ")
l.append("Appended Subject")
print(l)

print("insert function : ")
l.insert(3, "insertedSubject")
print(l)

print("remove function : ")
l.remove("insertedSubject")
print(l)

print("pop function : ")
poppedElement = l.pop()
print(l, "\n popped element is : ", poppedElement)

print("extendFunction : ")
extendList = ["CS41", "CS42", "CS43"]
l.extend(extendList)
print(l)
