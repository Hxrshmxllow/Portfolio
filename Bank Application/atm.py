import re

cardnum = 1234567890123456
realpin = 12345

class customer:
    def __init__(self):
        self.savingsRN = 0
        self.checkingsRN = 0
        self.savingsbalance = 0.00
        self.checkingsbalance = 0.00

def atmlogin():
    letters = re.compile("[a-zA-Z]")

    print("Welcome to the ATM!")

    cardnumIsValid = False
    while cardnumIsValid is False:
        try:
            debitcardnum = int(input("Debit Card Number: "))
            if len(str(debitcardnum)) != 16:
                print("Please enter a 16 digit number.")
            elif debitcardnum == cardnum:
                    cardnumIsValid = True
            else:
                print("Please enter a valid debit card number.")

        except ValueError:
             print("Please enter a 16 digit number.")

    pinIsValid = False
    while pinIsValid is False:
        try:
            pin = int(input("Pin: "))
            if len(str(pin)) < 4 or len(str(pin)) > 6:
                print("Please enter a 4 to 6 digit pin number.")
            elif pin == realpin:
                pinIsValid = True
            else:
                print("Pin does not match with your debit card number. Please try again.")
        except ValueError:
            print("Please enter a 4 to 6 digit pin number.")
    
    menu()

def menu():
    print("Welcome, Harshit!")
    print("What account would you like to access?")
    accounts = {
        "Savings": "Savings",
        "Checkings": "Checkings",
        "Enter a routing number": "Enter a routing number"
    }

    i = 1
    for account in accounts:
        if account is not "Enter a routing number":
            print(str(i) + ": " + accounts[account])
            i += 1
        

atmlogin()