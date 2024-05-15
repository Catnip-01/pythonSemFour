l = list(map(int, input("enter list : ").split()))
n = int(input("enter target : "))

def linearSearch(l, n, i):
       
    if i == len(l):
        print("element not in list") 
        exit()
    elif l[i] == n:
        print("element found at index : ", i)
        exit()
    linearSearch(l, n, i + 1)
linearSearch(l, n, 0)