class Loan:
    def __init__(self, loan_number, loan_amount, account_number, customer_id):
        self.loan_number = loan_number
        self.loan_amount = loan_amount
        self.account_number = account_number
        self.customer_id = customer_id

    def show_detail(self):
        return f"Loan Number: {self.loan_number} Loan Amount: {self.loan_amount}"