from tabulate import tabulate
from termcolor import cprint, colored
import os
import sys
import csv

def main():
    if os.path.exists("password-manager/login.csv") == False:
        password = input("You have to create a new account. Type your password here: ")
        conform_password = input("Conform password: ")
        if password == conform_password:
            with open("password-manager/login.csv", "w") as login:
               writer = csv.writer(login)
               writer.writerow([password])
            manager()
        else:
            sys.exit("The passwords do not match. User was not created!")
    else:
        login_password = input("Type your password: ")
        with open("password-manager/login.csv", "r") as file:
            for user in file:
                if login_password in user:
                    manager()
                else:
                    sys.exit("Wrong password!")
def manager():
    print("\nWelcome to the Password Manager!\n")
    headers = ["Number", "Setting"]
    table = [[1, "View passwords"], [2, "Add new password"], [3, "Delete a password"], [4, "Exit"]]
    print(tabulate(table, headers, tablefmt="grid"))
    while True:
        try:
            setting = int(input("Type the number of the setting you want to choose: "))
            break
        except ValueError:
            cprint("\nType a number!\n", "red")
            manager()
    
    if setting == 1:
        view_passwords()
    elif setting == 2:
        add_new_password()
    elif setting == 3:
        delete_password()
    elif setting == 4:
        sys.exit(colored("\nYou have exited the program!\n", "green"))
    else:
        cprint("\nInvalid setting!\n", "red")
        manager()
        
def view_passwords():
    headers = ["Name", "Password"]
    with open("passwords.csv", "r") as file:
        for i in file:
            ...
    
def add_new_password():
    with open("passwords.csv", "a"):
        ...

def delete_password():
    with open("passwords.csv", "a"):
        ...
    
main()