class Expense:
    def __init__(self,name, amount, category) -> None: #none means that it doesnot return anything as it is a constructor
        self.name = name
        self.amount = amount
        self.category = category
        self.amount = amount
    
    def __repr__(self):
        return f"Expense : {self.name}, {self.amount:.2f}, {self.category}"