from src.Entities.bank import Bank
from src.Entities.branch import Branch 
from src.Entities.customer import Customer 
import src.Infrastructures.terminal as terminal
from src.Persistences.repository import Repository

repository = Repository()
banks = repository.banks  
branches = repository.branches 
customers = repository.customers 

def create_new_bank():
    bank_id = len(banks) + 1
    bank_name = input("Enter bank name: ")
    banks[bank_id] = Bank(bank_id, bank_name)
    return banks[bank_id]

def create_new_branch(bank_id):
    branch_id = len(branches) + 1
    branch_name = input("Enter branch name: ")
    budget = int(input("Enter budget: "))
    city = input("Enter city: ")
    branches[branch_id] = Branch(bank_id, branch_id, branch_name, 0, budget, city)
    return branches[branch_id]

def create_new_customer(branch_id):
    customer_id = len(customers) + 1
    first_name = input("Enter customer first name: ")
    last_name = input("Enter customer last name: ")
    national_code = input("Enter customer national code: ")
    address = input("Enter customer address: ")
    branch = branches[branch_id]
    branch.number_of_customers += 1
    customers[customer_id] = Customer(branch_id, customer_id, first_name, last_name, national_code, address)
    return customers[customer_id]

def manage():
    while(True):
        try:
            print("Admin Menu:")
            print("1. Create New Bank")
            print("2. Create New Branch in a Bank")
            print("3. Create New Customer in a Branch")
            print("0. Back to Select Menu")
            choice = input("Enter your choice: ")
            terminal.clear()
            if choice == "1":
                bank = create_new_bank()
                print(terminal.GREEN, f"Bank '{bank.bank_name}' created with ID '{bank.bank_id}'.", terminal.RESET)
            elif choice == "2":
                for bank_id, bank in banks.items():
                    print(bank.show_detail())
                try:
                    bank_id = int(input("Enter bank ID to create branch: "))
                    if bank_id in banks:
                        branch = create_new_branch(bank_id)
                        print(terminal.GREEN, f"Branch '{branch.branch_name}' created in bank '{banks[bank_id].bank_name}'.", terminal.RESET)
                    else:
                        raise Exception("Bank not found.")
                except Exception as e:
                    print(terminal.RED, e, terminal.RESET)  
            elif choice == "3":
                for branch_id, branch in branches.items():
                    print(branch.show_detail())
                try:
                    branch_id = int(input("Enter branch id to create customer: "))
                    if branch_id in branches:
                        customer = create_new_customer(branch_id)
                        print(terminal.GREEN, f"Customer '{customer.first_name} {customer.last_name}' created in branch '{branches[branch_id].branch_name}'.", terminal.RESET)
                    else:
                        raise Exception("Branch not found.")
                except Exception as e:
                    print(terminal.RED, e, terminal.RESET)  
            elif choice == "0":
                break
            else:
                raise ValueError("Invalid choice. Please try again.")
        except ValueError as e:
            print(terminal.RED, e, terminal.RESET)