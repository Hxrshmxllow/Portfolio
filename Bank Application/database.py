import sqlite3
from account import customer

connection = sqlite3.connect("bank.db")
cursor = connection.cursor()

def createCustomersTable():
    cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               username VARCHAR NOT NULL,
               password VARCHAR NOT NULL,
               firstname VARCHAR NOT NULL,
               lastname VARCHAR NOT NULL,
               birthdate VARCHAR NOT NULL,
               ssn VARCHAR NOT NULL,
               debitcardnum INTEGER NOT NULL,
               creditcardnum INTEGER NULL
               )""")
    connection.commit()

def createAccountsTable():
    cursor.execute("""CREATE TABLE IF NOT EXISTS accounts (
               id INTEGER NOT NULL,
               routingnumber INTEGER NOT NULL,
               accountType VARCHAR NOT NULL,
               balance REAL NOT NULL
               )""")
    connection.commit()

def addCustomer():
    customerdata = (customer.username, customer.password, customer.firstname, customer.lastname, customer.birthdate, customer.ssn, customer.debitcardnum, customer.creditcardnum)
    cursor.execute("""INSERT INTO customers (username, password, firstname, lastname, birthdate, ssn) VALUES(?,?,?,?,?,?)""", customerdata)
    id = cursor.execute("""SELECT rowid from customers order by ROWID DESC limit 1""").fetchall()
    customer.id = id[0]
    savingsaccount = (customer.id, customer.savingsRN, "Savings", customer.savingsbalance)
    checkingsaccount = (customer.id, customer.checkingsRN, "Checkings", customer.checkingsbalance)
    cursor.execute("""INSERT INTO accounts VALUES(?,?,?,?)""", savingsaccount)
    cursor.execute("""INSERT INTO accounts VALUES(?,?,?,?)""", checkingsaccount)
    connection.commit()

def findCustomer(username, password):
    data = (username, password)
    customerinfo = cursor.execute("""SELECT * FROM customers WHERE username = ? and password = ?""", data).fetchall()
    if len(customerinfo) == 0:
        return False
    else:
        customer.id = customerinfo[0][0]
        customer.username = customerinfo[0][1]
        customer.password = customerinfo[0][2]
        customer.firstname = customerinfo[0][3]
        customer.lastname = customerinfo[0][4]
        customer.birthdate = customerinfo[0][5]
        customer.ssn = customerinfo[0][6]
        findAccounts()
        return True
    
def findAccounts():
    accounts = cursor.execute("""SELECT * FROM accounts WHERE id = ?""", customer.id).fetchall()
    for account in accounts:
        if account[2] == "Savings":
            customer.savingsRN = account[1]
            customer.savingsbalance = account[3]
        elif account[2] == "Checkings":
            customer.checkingsRN = account[1]
            customer.checkingsbalance = account[3]
    return

def validateATM(debitcardnum, pin):
    cardnumbers = cursor.execute("""SELECT * customers WHERE debitcardnum = ?""", (debitcardnum)).fetchall()
    print(cardnumbers)

#createCustomersTable()
#createAccountsTable()
validateATM(1,1)