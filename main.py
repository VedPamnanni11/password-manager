import os
import sys
import csv

def main():
    if os.path.exists("login.csv") == False:
        password = input("You have to create a new account. Type your password here: ")
        conform_password = input("Conform password: ")
        if password == conform_password:
            with open("login.csv", "w") as login:
               writer = csv.DictWriter(login, fieldnames=["password"])
               writer.writeheader()
               writer.writerow({"password": password}) 
        else:
            ...
    else:
        ...    
    
    
main()