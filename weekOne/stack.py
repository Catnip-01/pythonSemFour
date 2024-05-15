class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1
    
    def push(self, item):
        self.stack.append(item)
        self.top += 1

    def peek(self):
        print(self.stack[self.top])

    def pop(self):
        del self.stack[self.top]
        self.top -= 1

    def isEmpty(self):
        if (self.top == -1):
            print("empty")
        else:
            print("not empty")

    


s = Stack()


while True:
    choice = input("enter choice : ")
    if choice == "push":
        item = input("enter element : ")
        s.push(item)
    elif choice == "pop":
        s.pop()
    elif choice == "isEmpty":
        s.isEmpty()
    elif choice == "peek":
        s.peek()
    else:
        print("incorrect choice entered!")