import sqlite3
from database import findCustomer

def login():
    customerexists = False
    while customerexists == False:
        username = input("Username: ")
        password = input("Password: ")
        customerexists = findCustomer(username, password)
        if customerexists:
            print("Logging in...")
            print("--------------------------")
            return True
        else:
            print("Username and password don't match. Please try again.")
            register = input("Would you like to register an account (y/n)? ")
            if "y" in register:
                return False
            else:
                print("--------------------------")