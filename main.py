from src.Entities.bank import Bank
from src.Entities.branch import Branch 
from src.Entities.customer import Customer 
import os

def main_menu():
    print("Main Menu:")
    print("1. Create New Bank")
    print("2. Create New Branch in a Bank")
    print("3. Create New Customer in a Branch")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice


def clear_terminal():
    if os.name == 'nt':  # windows
        os.system('cls')
    else:  # linux/mac
        os.system('clear')  


def create_new_bank():
    bank_id = input("Enter bank ID: ")
    bank_name = input("Enter bank name: ")
    return Bank(bank_id, bank_name)

def create_new_branch(bank):
    branch_id = input("Enter branch ID: ")
    branch_name = input("Enter branch name: ")
    budget = float(input("Enter budget: "))
    city = input("Enter city: ")
    return Branch(branch_id,bank.bank_id, branch_name, 0, budget, city)

def create_new_customer(branch):
    customer_id = input("Enter customer ID: ")
    first_name = input("Enter customer first name: ")
    last_name = input("Enter customer last name: ")
    national_code = input("Enter customer national code: ")
    address = input("Enter customer address: ")
    return Customer(branch.get_branch_id(), customer_id, first_name, last_name, national_code, address)

def main():
    banks = []  
    branches = [] 
    customers = []  
    while True:
        choice = main_menu()
        clear_terminal()
        if choice == "1":
            bank = create_new_bank()
            banks.append(bank)
            print(f"Bank '{bank.bank_name}' created with ID '{bank.bank_id}'.")
        elif choice == "2":
            for bank in banks:
                print(bank.show_detail())
            bank_id = input("Enter bank ID to create branch: ")
            bank = next((b for b in banks if b.bank_id == bank_id), None)
            if bank:
                branch = create_new_branch(bank)
                branches.append(branch)
                print(f"Branch '{branch.branch_name}' created in bank '{bank.bank_name}'.")
            else:
                print("Bank not found.")
        elif choice == "3":
            for branch in branches:
                print(branch.show_detail())
            branch_id = input("Enter branch id to create customer: ")
            branch = next((b for b in branches if b.branch_id == branch_id), None)
            if branch:
                customer = create_new_customer(branch)
                customers.append(customer)
                print(f"Customer '{customer.first_name} {customer.last_name}' created in branch '{branch.get_branch_name()}'.")
            else:
                print("Branch not found.")
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
