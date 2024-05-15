# s1 = int(input("enter marks of subject 1: "))
# s2 = int(input("enter marks of subject 2: "))
# s3 = int(input("enter marks of subject 3: "))
# s4 = int(input("enter marks of subject 4: "))

def grade(marks):
    if (marks > 90 and marks <= 100):
        return "S"
    elif (marks > 80 and marks <= 90):
        return "A"
    elif marks > 70 and marks <= 80:
        return "B"
    elif marks > 60 and marks <= 70:
        return "C"
    elif marks > 50 and marks <= 60:
        return "D"
    elif marks >= 0 and marks <= 40:
        return "F"
    elif marks > 40 and marks <= 50:
        return "E"
    else :
        return ("invalid marks entered !")

# print("subject 1 grade : ", grade(s1))
# print("subject 2 grade : ", grade(s2))
# print("subject 3 grade : ", grade(s3))
# print("subject 4 grade : ", grade(s4))

for i in range(4):
    n = int(input(f"enter marks of subject {i + 1} : "))
    print(f"marks of {i + 1} are : {grade(n)}")