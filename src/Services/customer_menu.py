from src.Persistences.repository import Repository
import src.Infrastructures.terminal as terminal

repository = Repository()
customers = repository.customers 

def manage():
    while(True):
        try:
            print("Customer Menu:")
            print("1. Open an Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Request Loan")
            print("0. Back to Select Menu")
            choice = input("Enter your choice: ")
            terminal.clear()
            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "0":
                break
            else:
                raise ValueError("Invalid choice. Please try again.")
        except ValueError as e:
            print(terminal.RED, e, terminal.RESET)