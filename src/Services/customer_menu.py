import src.Infrastructures.terminal as terminal
import src.Infrastructures.unique_number as unique_number

def show_accounts(accounts):
    for account_number, account in accounts.items():
        print(account.show_detail())

def choose_accounts(accounts):
    account_number = input("Choose Account Number: ")
    if account_number in accounts:
        account = accounts[account_number]
        return account
    else:
        raise Exception("Account not found.")

def check_budget_for_loan(loan_amount, budget):
    if loan_amount > budget:
        raise Exception("Insufficient budget in the branch for the requested loan amount.")

def manage(customer, branch):
    while(True):
        try:
            print("Customer Menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Accounts Details")
            print("4. Request Loan")
            print("5. Show Loan Detail")
            print("0. Back to Select Menu")
            choice = input("Enter your choice: ")
            terminal.clear()
            if choice == "1":
                show_accounts(customer.accounts)
                try:
                    account = choose_accounts(customer.accounts)
                    amount = int(input("Enter Deposit Amount: "))
                    account.deposit(amount)
                    print(f"Amount {amount} successfully Deposit / New Balance: {account.balance}")
                except Exception as e:
                    print(terminal.RED, e, terminal.RESET)  
            elif choice == "2":
                show_accounts(customer.accounts)
                try:
                    account = choose_accounts(customer.accounts)
                    amount = int(input("Enter Withdraw Amount: "))
                    if(amount <= account.balance):
                        account.withdraw(amount)
                        print(f"Amount {amount} successfully Withdraw / New Balance: {account.balance}")
                    else:
                        raise Exception("insufficient balance.")
                except Exception as e:
                    print(terminal.RED, e, terminal.RESET)  
            elif choice == "3":
                show_accounts(customer.accounts)
            elif choice == "4":
                try:
                    if(customer.loan != None):
                        raise Exception("You Have already requested loan recently in this branch")
                    show_accounts(customer.accounts)
                    account = choose_accounts(customer.accounts)
                    loan_amount = int(input("Enter Your Loan Request Amount: "))
                    check_budget_for_loan(loan_amount, branch.budget)
                    loan_number = unique_number.generate()
                    account_number = account.account_number
                    customer.request_loan(loan_number, loan_amount, account_number) 
                    branch.budget -= loan_amount
                    account.balance += loan_amount
                    print('---------------------------------------------------------------------')
                    print(f"Loan request with Laon Number {loan_number} and amount {loan_amount} is successfully registered")
                    print(f"Account balance: {account.balance} ")
                    print('---------------------------------------------------------------------')
                except Exception as e:
                    print(terminal.RED, e, terminal.RESET)  
            elif choice == "5":
                if customer.loan != None:
                    print(customer.loan.show_detail())
                else:
                    print("Customer hasn't applied for any loan yet")
            elif choice == "0":
                break
            else:
                raise ValueError("Invalid choice. Please try again.")
        except ValueError as e:
            print(terminal.RED, e, terminal.RESET)