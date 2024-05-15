a = int(input("enter number 1 : "))
b = int(input("enter number 2 : "))

while True:
    choice = input("enter operation : ")
    if choice == "add":
        print(a + b)
    elif choice == "subtract":
        print(a - b)
    elif choice == "multiply":
        print(a*b)
    elif choice == "divide":
        print(a/b)
    elif choice == "exit":
        exit()
    else:
        print("enter proper choice !!!")