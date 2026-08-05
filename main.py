from tabulate import tabulate
import os
import sys
import csv

def main():
    if os.path.exists("login.csv") == False:
        password = input("You have to create a new account. Type your password here: ")
        conform_password = input("Conform password: ")
        if password == conform_password:
            with open("login.csv", "w") as login:
               writer = csv.writer(login)
               writer.writerow([password])
            manager()
        else:
            sys.exit("The passwords do not match. User was not created!")
    else:
        login_password = input("Type your password: ")
        with open("login.csv", "r") as file:
            for user in file:
                if login_password in user:
                    manager()
                else:
                    sys.exit("Wrong password!")
def manager():
    ...
    
main()