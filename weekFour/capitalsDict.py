d = {
    "Karnataka" : "Bangalore",
    "Maharashtra" : "Mumbai",
    "TamilNadu" : "Chennai"
}

print(d.keys())
print(d.values())
print(d.items())
print(d.get("Karnataka"))
print(d)

other_capitals = {"Gujarat" : "Gandhinagar"}
d.update(other_capitals)

print(d)
print(other_capitals)