class Queue:
    def __init__ (self):
        self.front = -1
        self.rear = -1
        self.items = []
    def enQueue(self, item):
        if self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
            # print("entered this clause and self.rear = ", self.rear)

        elif self.front == 0 and self.rear == 0:
            self.rear += 1
        else:
            self.rear += 1
        self.items.append(item)
    def deQueue(self):
        if (self.front == self.rear == -1):
            print("queue is empty")
        else:
            print("deQueued item : ", self.items[self.front])
            self.front += 1
    def display(self):
        if (self.front == self.rear == -1):
            print("queue is empty")
        else:
            for i in range(self.front, self.rear + 1):
                print("item : ", self.items[i])
    
q = Queue()

while True:
    choice = input("enter choice : ")
    if (choice == "enQueue"):
        item = input("enter item : ")
        
        q.enQueue(item)
        # print(q.rear)
    elif choice == "deQueue":
        q.deQueue()
    elif choice == "display":
        q.display()
    else:
        print("entered incorrect choice")
