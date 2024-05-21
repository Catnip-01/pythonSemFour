d = {
    "Rahul" : "genius",
    "Kumar" : "smart",
    "Ankita" : "intelligent"
}

print(d.items())
print(d.keys())
print(d.values())

for i in d.keys():
    print(i, d[i])
d["Ankita"] = "brilliant"

print(d)
