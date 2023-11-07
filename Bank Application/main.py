from account import customer
from register import register
from home import menu
from database import addCustomer
from login import login

def main():
    if login() is False:
        register()
        addCustomer()
    menu()

if __name__ == "__main__":
    main()