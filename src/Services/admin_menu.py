from src.Entities.bank import Bank
from src.Entities.branch import Branch 
from src.Entities.customer import Customer 
import src.Infrastructures.colors as colors

def create_new_bank(banks):
    bank_id = str(len(banks) + 1)
    bank_name = input("Enter bank name: ")
    return Bank(bank_id, bank_name)

def create_new_branch(bank,branches):
    branch_id = str(len(branches) + 1)
    branch_name = input("Enter branch name: ")
    budget = float(input("Enter budget: "))
    city = input("Enter city: ")
    return Branch(branch_id,bank.bank_id, branch_name, 0, budget, city)

def create_new_customer(branch,customers):
    customer_id = str(len(customers) + 1)
    first_name = input("Enter customer first name: ")
    last_name = input("Enter customer last name: ")
    national_code = input("Enter customer national code: ")
    address = input("Enter customer address: ")
    return Customer(branch.branch_id, customer_id, first_name, last_name, national_code, address)

def show():
    print("Main Menu:")
    print("1. Create New Bank")
    print("2. Create New Branch in a Bank")
    print("3. Create New Customer in a Branch")
    print("4. Back to Main Menu")
    choice = input("Enter your choice: ")
    return choice

def manage(choice, banks, branches, customers):
    try:
        if choice == "1":
            bank = create_new_bank(banks)
            banks.append(bank)
            print(colors.GREEN, f"Bank '{bank.bank_name}' created with ID '{bank.bank_id}'.", colors.RESET)
        elif choice == "2":
            for bank in banks:
                print(bank.show_detail())
            try:
                bank_id = input("Enter bank ID to create branch: ")
                bank = next((b for b in banks if b.bank_id == bank_id), None)
                if bank:
                    branch = create_new_branch(bank,branches)
                    branches.append(branch)
                    print(colors.GREEN, f"Branch '{branch.branch_name}' created in bank '{bank.bank_name}'.", colors.RESET)
                else:
                    raise Exception("Bank not found.")
            except Exception as e:
                print(colors.RED, e, colors.RESET)  
        elif choice == "3":
            for branch in branches:
                print(branch.show_detail())
            try:
                branch_id = input("Enter branch id to create customer: ")
                branch = next((b for b in branches if b.branch_id == branch_id), None)
                if branch:
                    customer = create_new_customer(branch,customers)
                    customers.append(customer)
                    print(colors.GREEN, f"Customer '{customer.first_name} {customer.last_name}' created in branch '{branch.branch_name}'.", colors.RESET)
                else:
                    raise Exception("Branch not found.")
            except Exception as e:
                print(colors.RED, e, colors.RESET)  
        elif choice == "4":
            return
        else:
            raise ValueError("Invalid choice. Please try again.")
    except ValueError as e:
        print(colors.RED, e, colors.RESET)  
