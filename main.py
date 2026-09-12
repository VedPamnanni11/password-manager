from tabulate import tabulate
from termcolor import cprint, colored
import os
import sys
import csv

def main():
    if os.path.exists("passwords.csv") == False:
        password = input("You have to create a new account. Type your password here: ")
        conform_password = input("Conform password: ")
        if password == conform_password:
            manager(password)
        else:
            sys.exit(colored("\nThe passwords do not match. User was not created!\n", "red"))
    else:
        login_password = input("Type your password: ")
        with open("passwords.csv", "r") as file:
            ...

def manager(password):
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
            manager(password)
    
    if setting == 1:
        view_passwords()
    elif setting == 2:
        add_new_password(password)
    elif setting == 3:
        delete_password()
    elif setting == 4:
        sys.exit(colored("\nYou have exited the program!\n", "green"))
    else:
        cprint("\nInvalid setting!\n", "red")
        manager(password)
        
def view_passwords():
    try:
        with open("passwords.csv", "r") as file:
            ...
    except FileNotFoundError:
        sys.exit(colored("\nYou have no passwords to view.\n", "red"))
    
def add_new_password(password):
    if os.path.exists("passwords.csv") == False:
        with open("passwords.csv", "w") as head:
            info = csv.DictWriter(head, fieldnames=["Website", "Username", "Password"])
            info.writeheader()
            info.writerow({"Website": "PassMan", "Username": "N/A", "Password": password})

    with open("passwords.csv", "a") as file:
        ...

def delete_password():
    with open("passwords.csv", "a") as file:
        ...
    
if __name__ == "__main__":
    main()