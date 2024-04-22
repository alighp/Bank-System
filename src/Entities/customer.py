from src.Entities.person import Person
from src.Entities.account import Account
from src.Entities.loan import Loan

class Customer(Person):
    def __init__(self, branch_id, customer_id, first_name, last_name, national_code, address):
        super().__init__(first_name, last_name)
        self.branch_id = branch_id
        self.customer_id = customer_id
        self.national_code = national_code
        self.address = address
        self.accounts = {}
        self.loan = None

    def open_account(self, bank_id, unique_number):
        account_number = f"{bank_id:02d}{self.branch_id:02d}{unique_number:04d}" 
         # Assuming max 99 banks and branches, 9999 customers
        new_account = Account(self.customer_id, account_number)
        self.accounts[account_number] = new_account
        return new_account

    def show_detail(self):
        return f"Customer ID: {self.customer_id}\
        First Name: {self.first_name}\
        Last Name: {self.last_name}\
        National Code: {self.national_code}\
        Address: {self.address}"

    def request_loan(self, loan_number, loan_amount, account_number):
        loan = Loan(loan_number, loan_amount, account_number, self.customer_id)
        self.loan = loan
        return loan
