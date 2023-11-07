from account import customer
from login import login
from transactions import transfer

currentAccount = ""

def printinfo():
    print("--------------------------")
    print("First Name: " + customer.firstname)
    print("Last Name: " + customer.lastname)
    print("Birthdate: " + customer.birthdate)
    print("Social Security Number: " + customer.ssn)
    print("Username: " + customer.username)
    print("Password: " + customer.password)
    print("--------------------------")

def menu():
    print("Welcome, " + customer.firstname + "!")

    print("Which account would you like to access?")
    accounts = {
        1: "Savings",
        2: "Checkings"
    }

    print("Which account would you like to tranfer money from?")
    for key in accounts.keys():
        print(str(key) + ":" + options[key])
    
    while True:
        try:
            userinput = int(input("Enter your choice: "))
            break
        except ValueError:
            print("Please enter a number from the available options.")

    currentAccount = accounts[userinput]

    print("--------------------------")
    print("What would you like to do?")

    options = {
        1: "Update Account Info",
        2: "View Balance",
        3: "Transfer Money",
        4: "Switch Accounts",
        5: "Log Out"
    }

    for key in options.keys():
        print(str(key) + ": " + options[key])

    while True:
        try:
            userinput = int(input("Enter your choice: "))
            break
        except ValueError:
            print("Please enter a number from the available options.")

    if userinput == 1:
        updateAccountInfo()
    elif userinput == 2:
        viewBalance()
    elif userinput == 3:
        transfer()
    elif userinput == 4:
        switchAccounts()
    else:
        login()

  
def updateAccountInfo():
    return

def viewBalance():
    return

def switchAccounts():
    return