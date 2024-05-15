studentInfo = {}
d = {}
n = int(input("enter number of students : "))

for i in range(1, n + 1):
    key = f"Student{i}"
    d[key] = {
    "usn" : int(input("enter usn : ")),
    "name" : input("enter name : "),
    "dob" : input("enter dob : "),
    "phone" : int(input("enter phone number : ")),
    "address" : input("enter address : "),
    "10th" : float(input("enter 10th percentage : ")),
    "12th" : float(input("12th percentage : "))
}
    
for i in range(1, n + 1):
    key = f"Student{i}"
    print(f"Student {i} : {d[key]}")
# studentInfo["student" + ""] = {
#     "usn" : input("enter usn : "),
#     "name" : input("enter name : "),
#     "dob" : input("enter dob : "),
#     "phone" : input("enter phone number : "),
#     "address" : input("enter address : "),
#     "10th" : input("enter 10th percentage : "),
#     "12th" : input("12th percentage : ")
# }
# studentInfo["student2"] = {
#     "usn" : input("enter usn : "),
#     "name" : input("enter name : "),
#     "dob" : input("enter dob : "),
#     "phone" : input("enter phone number : "),
#     "address" : input("enter address : "),
#     "10th" : input("enter 10th percentage : "),
#     "12th" : input("12th percentage : ")
# }
# studentInfo["student3"] = {
#     "usn" : input("enter usn : "),
#     "name" : input("enter name : "),
#     "dob" : input("enter dob : "),
#     "phone" : input("enter phone number : "),
#     "address" : input("enter address : "),
#     "10th" : input("enter 10th percentage : "),
#     "12th" : input("12th percentage : ")
# }
# print(studentInfo)
# print(f"{d["Student1"].keys()} : {d["student1"].values()}")