import src.Services.admin_menu as admin_menu
import src.Services.customer_menu as customer_menu
import json
from getpass import getpass
import src.Infrastructures.terminal as terminal
import src.Infrastructures.file as file

banks = {}
branches = {}
customers = {}

def main():
    while True:
        print("Select Menu:")
        print("1. Admin Menu")
        print("2. Customer Menu")
        print("0. Exit")
        menu_choice = input("Enter your choice: ")
        terminal.clear()
        if menu_choice == '1':
            admin_credentials = file.load_admin_credentials('admin_credentials.json')
            username = input("Enter username: ")
            password = getpass("Enter password: ")

            if username == admin_credentials['username'] and \
             password == admin_credentials['password']:
                terminal.clear()
                print(terminal.GREEN, "Login successful. Access granted to admin menu.", terminal.RESET)
                admin_menu.manage(banks, branches, customers)
            else:
                terminal.clear()
                print(terminal.RED, "Invalid username or password. Access denied.", terminal.RESET)
                continue 

        elif menu_choice == '2':
            for customer_id, customer in customers.items():
                print(customer.show_detail())
            try:
                national_code = input("Enter customer national code: ")  
                for customer_id, customer in customers.items():
                    if customer.national_code == national_code:
                        branch = branches[customer.branch_id]
                        print('---------------------------------------------------')
                        print(terminal.GREEN, f"hello {customer.first_name} {customer.last_name}, Welcome!", terminal.RESET)
                        print('---------------------------------------------------')
                        customer_menu.manage(customer, branch)
                        break
                raise Exception("Customer not found.")
            except Exception as e:
                print(terminal.RED, e, terminal.RESET)  
        elif menu_choice == '0':
            break
        else:
            print(terminal.RED, "Invalid choice. try again.", terminal.RESET)
    terminal.clear()

main()
