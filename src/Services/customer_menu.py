import src.Infrastructures.terminal as terminal

def show_accounts(accounts):
    for account_number, account in accounts.items():
        print(account.show_detail())

def choose_accounts():
    return input("Choose Account Number: ")

def manage(customer):
    while(True):
        try:
            print("Customer Menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Accounts")
            print("4. Request Loan")
            print("0. Back to Select Menu")
            choice = input("Enter your choice: ")
            terminal.clear()
            if choice == "1":
                show_accounts(customer.accounts)
                account_number = choose_accounts()
                try:
                    if account_number in customer.accounts:
                        account = customer.accounts[account_number]
                        amount = int(input("Enter Deposit Amount: "))
                        account.deposit(amount)
                        print(f"Amount {amount} successfully Deposit / New Balance: {account.balance}")
                    else:
                        raise Exception("Account not found.")
                except Exception as e:
                    print(terminal.RED, e, terminal.RESET)  
            elif choice == "2":
                show_accounts(customer.accounts)
                account_number = choose_accounts()
                try:
                    if account_number in customer.accounts:
                        account = customer.accounts[account_number]
                        amount = int(input("Enter Withdraw Amount: "))
                        account.withdraw(amount)
                        print(f"Amount {amount} successfully Withdraw / New Balance: {account.balance}")
                    else:
                        raise Exception("Account not found.")
                except Exception as e:
                    print(terminal.RED, e, terminal.RESET)  
            elif choice == "3":
                show_accounts(customer.accounts)
            elif choice == "4":
                pass    
            elif choice == "0":
                break
            else:
                raise ValueError("Invalid choice. Please try again.")
        except ValueError as e:
            print(terminal.RED, e, terminal.RESET)