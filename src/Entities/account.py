class Account:
    def __init__(self, customer_id, account_number):
        self.account_number = account_number
        self.customer_id = customer_id
        self.balance = 50000 #initial account balance 50000 toman 

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

    def show_detail(self):
        return f"Account Number: {self.account_number} Balance: {self.balance}"