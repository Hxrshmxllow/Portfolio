class Account:
    def __init__(self):
        self.id = 0
        self.username = ""
        self.password = ""
        self.firstname = ""
        self.lastname = ""
        self.birthdate = ""
        self.ssn = ""
        self.savingsRN = 0 #savingsRoutingNumber
        self.savingsbalance = 0.00
        self.checkingsRN = 0 #checkingsRoutingNumber
        self.checkingsbalance = 0.00
        self.pin = 0
        self.debitcardnum = 0
        self.creditcardnum = 0
    
    def withdrawSavings(self, amount):
        self.savingsbalance -= amount

    def withdrawCheckings(self, amount):
        self.checkingsbalance -= amount

    def depositSavings(self, amount):
        self.savingsbalance += amount
    
    def depositCheckings(self, amount):
        self.checkingsbalance += amount

customer = Account()
