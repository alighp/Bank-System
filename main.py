import src.Services.admin_menu as admin_menu
import src.Services.customer_menu as customer_menu
import json
from getpass import getpass

import src.Infrastructures.terminal as terminal



def load_admin_credentials(filename):
    with open(filename, 'r') as file:
        credentials = json.load(file)
    return credentials

def main():
    while True:
        print("Select Menu:")
        print("1. Admin Menu")
        print("2. Customer Menu")
        print("0. Exit")
        menu_choice = input("Enter your choice: ")
        terminal.clear()
        if menu_choice == '1':
            admin_credentials = load_admin_credentials('admin_credentials.json')
            username = input("Enter username: ")
            password = getpass("Enter password: ")

            if username == admin_credentials['username'] and \
             password == admin_credentials['password']:
                terminal.clear()
                print(terminal.GREEN, "Login successful. Access granted to admin menu.", terminal.RESET)
                admin_menu.manage()
            else:
                terminal.clear()
                print(terminal.RED, "Invalid username or password. Access denied.", terminal.RESET)
                continue 

        elif menu_choice == '2':
            customer_menu.manage()
            pass
        elif menu_choice == '0':
            break
        else:
            print(terminal.RED, "Invalid choice. Please enter '1' or '2'.", terminal.RESET)
    terminal.clear()

main()
