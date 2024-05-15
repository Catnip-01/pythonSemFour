l = list(map(int, input("enter list : ").split()))
n = int(input("enter target : "))

l.sort()
print(l)

def binSearch(l, n, start, end):
    if (start >= end):
        print("not found")
        exit()
    mid = (start+end)//2
    if l[mid] == n:
        print("element found at : ", mid)
        exit()
    elif (l[mid] < n):
        binSearch(l, n, mid+1, end)
    else:
        binSearch(l, n, start, mid - 1)
binSearch(l, n, 0, len(l))
