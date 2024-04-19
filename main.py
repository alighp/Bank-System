import src.Services.admin_menu as admin_menu
import json
from getpass import getpass
import os
import src.Infrastructures.colors as colors

banks = []  
branches = [] 
customers = []  


def clear_terminal():
    if os.name == 'nt':  # windows
        os.system('cls')
    else:  # linux/mac
        os.system('clear') 

def load_admin_credentials(filename):
    with open(filename, 'r') as file:
        credentials = json.load(file)
    return credentials

def main():
    while True:
        print("Select Menu:")
        print("1. Admin Menu")
        print("2. Customer Menu")
        print("3. Exit")
        menu_choice = input("Enter your choice: ")
        clear_terminal()
        if menu_choice == '1':
            admin_credentials = load_admin_credentials('admin_credentials.json')
            username = input("Enter username: ")
            password = getpass("Enter password: ")

            if username == admin_credentials['username'] and \
             password == admin_credentials['password']:
                clear_terminal()
                print(colors.GREEN, "Login successful. Access granted to admin menu.", colors.RESET)
                choice = admin_menu.show()
                clear_terminal()
                admin_menu.manage(choice, banks, branches, customers)
            else:
                clear_terminal()
                print(colors.RED, "Invalid username or password. Access denied.", colors.RESET)
                continue 

        elif menu_choice == '2':
            pass
        elif menu_choice == '3':
            break
        else:
            print(colors.RED, "Invalid choice. Please enter '1' or '2'.", colors.RESET)

main()
