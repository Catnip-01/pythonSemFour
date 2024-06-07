class Invoice:
    def __init__(self, items, type, price):
        self.items = items
        self.type = type
        self.price = price
    def calcTax(self):
        for i in range(len(self.items)):
            if self.type[i] == 1:
                taxRate = .05
            elif self.type[i] == 2:
                taxRate = .12
            elif self.type[i] == 3:
                taxRate = .18
            elif self.type[i] == 4:
                taxRate = .28
                
            tax[i] = price[i] * taxRate
        totalTax = sum(tax)
        return totalTax  
        
    def printInvoice(self):
        
            
            