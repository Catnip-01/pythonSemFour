d = {
    "hey" : "greeting",
    "hello" : "greeting",
    "byebye" : "bye",
    "ik" : "i know"
}

def searchWord():

    s = input("which word's meaning do you want? : ")
    print(f"meaning of {s} is : {d[s]}")
    
def sameMeaning():
    
    x = "hi"
    for i in d.keys:
        if (d[i] == x):
            print(i)
        
def removeMeaning():
    s = input("enter which meaning you want to remove : ")
    d.popitem(s)
    
def sort():
    d.sort()
    print(d)
    
flag = 1

while (flag):
    
    choice = input("enter choice : ")

    if (choice == "search"):
        searchWord()
    elif (choice == "same"):
        sameMeaning()
    elif choice == "remove":
        removeMeaning()
    elif choice == "sort":
        sort()
    elif choice == "exit":
        flag = 0
    else:
        print("enter proper choice !")