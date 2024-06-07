class Employee:
    def __init__(self, id, name, designation, experience, age):
        self.id=  id
        self.name = name
        self.designation = designation
        self.experience = experience
        self.age = age
    
    def addEmp(self, id, name, designation, experience, age):
        self.id = id
        self.name = name
        self.age = age
        self.designation = designation
        self.experience = experience
        self.age = age
        
    def displayDetails(self):
        print(f"details are : \nid : {self.id}\nname : {self.name}\ndesignation : {self.designation}\nage : {self.age}\nexperience : {self.experience}")
        
    def calcSalary(self, basic):
        if (self.age < 30 and self.experience > 5):
            print(f"salary is : {basic*1.5}")
        elif (self.age < 40 and self.experience > 5):
            print(f"salary is : {basic*1.5}")
        elif (self.age < 40 and self.experience > 10):
            print(f"salary is : {basic*1.5}")
        elif (self.age < 50 and self.experience > 20):
            print(f"salary is : {basic*1.5}")            
        elif (self.age < 50 and self.experience > 25):
            print(f"salary is : {basic*1.5}")         
        elif (self.age < 58 and self.experience > 30):
            print(f"salary is : {basic*1.5}")
            
emp1 = Employee(123, "Shantanu", "student intern", 12, 21)
emp1.displayDetails()
emp1.calcSalary(1000)