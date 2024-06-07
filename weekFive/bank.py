class BankAccount:
    def __init__(self, name, accNum, balance, type, add):
        self.name = name
        self.accNum = accNum
        self.balance = balance
        self.type = type
        self.add = add
        
    def withdraw(self, amount):
        if (self.balance < amount):
            print("insufficient funds !")
            return 
        self.balance = self.balance - amount
        print("successfully withdrawn ", amount, " amount.")
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        
    def displayDetails(self):
        print(f"""name : {self.name}\naccount number : {self.accNum}\nbalance : {self.balance}\naccount type : {self.type}\naddress : {self.add}
            """)
acc1 = BankAccount("Shantanu", 123, 1000, "savings", "negro arroya lane")

acc1.withdraw(1000)
acc1.deposit(10)
print("account 1 details : ")
acc1.displayDetails()