from account import customer
import re
import random

def register():
    numbers = re.compile("[0-9]")
    specialchar = re.compile("[@_!#$%^&*()<>?/|}{~:]")
    letters = re.compile("[a-zA-Z]")
    bdayFormat = re.compile("[0-9]{2}/[0-9]{2}/[0-9]{4}")

    #ask for firstname
    validInput = False
    while validInput == False:
        firstname = input("Enter your first name: ")
        if numbers.search(firstname) or specialchar.search(firstname):
            print("Your first name cannot contain and numbers or special characters")
        else:
            customer.firstname = firstname.title()
            validInput = True

    #ask for lastname
    validInput = False
    while validInput == False:
        lastname = input("Enter your last name: ")
        if numbers.search(lastname) or specialchar.search(lastname):
            print("Your lastname name cannot contain and numbers or special characters")
        else:
            customer.lastname = lastname.title()
            validInput = True

    #ask for birthdate
    validInput = False
    while validInput == False:
        birthdate = input("Enter your birthdate (mm/dd/yyyy): ")
        if letters.search(birthdate):
            print("Your birthdate must be in mm/dd/yyyy format and cannot contain any letters")
        elif bdayFormat.match(birthdate):
            customer.birthdate = birthdate
            validInput = True
    
    #ask for ssn
    validInput = False
    while validInput == False:
        ssn = input("Enter your social security number: ")
        if letters.search(ssn) or specialchar.search(ssn) or len(ssn) != 10:
            print("Your ssn name cannot contain letters or special characters and has to be 10 numbers")
        else:
            customer.ssn = ssn
            validInput = True

    #ask for username
    validInput = False
    while validInput == False:
        username = input("Enter a username: ")
        if (numbers.search(username) or letters.search(username)):
            customer.username = username
            validInput = True
        elif specialchar.search(lastname):
            print("Your username name has to contain letters and numbers but no special characters")
        

    #ask for password
    validInput = False
    while validInput == False:
        password = input("Enter a password: ")
        if (numbers.search(password) or letters.search(password) or specialchar.search(password)):
            customer.password = password
            validInput = True
        else:
            print("Your password name has to contain letters, numbers, and special characters")

    validInput = False
    while validInput == False:
        try:
            pin = int(input("Enter a 4 to 6 digit pin number: "))
            if len(pin) < 4 or len(pin) > 6:
                print("Your pin has to be 4 to 6 digits and cannot contain letters and special characters")
            else:
                customer.pin = pin
                validInput = True
        except ValueError:
                print("Your pin has to be 4 to 6 digits and cannot contain letters and special characters")
    
    #auto generate account info
    minimum = pow(10, 9)
    maximum = pow(20, 10) - 1

    savingsRN = random.randint(minimum, maximum)
    checkingsRN = random.randint(minimum, maximum)
    customer.savingsRN = savingsRN
    customer.checkingsRN = checkingsRN
    customer.debitcardnum = random.randint(pow(10,16), pow(20, 16) - 1)
    
    #print out info
    print("--------------------------")
    print("First Name: " + customer.firstname)
    print("Last Name: " + customer.lastname)
    print("Birthdate: " + customer.birthdate)
    print("Social Security Number: " + customer.ssn)
    print("Username: " + customer.username)
    print("Password: " + customer.password)
    print("Pin: " + str(customer.pin))
    print("Savings Account Routing Number: " + str(customer.savingsRN))
    print("Checkings Account Routing Number: " + str(customer.checkingsRN))
    print("Debit Card Number: " + str(customer.debitcardnum))
    print("--------------------------")
