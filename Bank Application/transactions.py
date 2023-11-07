import sqlite3
from account import customer
from home import currentAccount

connection = sqlite3.connect("bank.db")
cursor = connection.cursor()

def createTransactionsTable():
    cursor.execute("""CREATE TABLE IF NOT EXISTS transactions (
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               routingnumber INTEGER NOT NULL,
               type VARCHAR NOT NULL,
               amount REAL NOT NULL,
               description VARCHAR
               )""")
    connection.commit()

def withdraw():
    return

def transfer():
    transferFrom = currentAccount
    options = {
        "Savings": "Savings",
        "Checkings": "Checkings",
        "Enter a routing number": "Enter a routing number"
    }
    options.pop(transferFrom)
    i = 1
    for option in options:
        print(str(i) + ": " + options[option])
        i += 1

    while True:
        try:
            option = int(input("Enter your choice: "))
            break
        except ValueError:
            print("Please enter a number from the available options.")

    if option == 1:
        transferTo = options[1]
    else:
        transferTo = int(input("Enter the routing number of the account you would like to transfer to: "))
    


#createTransactionsTable()