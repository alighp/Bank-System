class Bank:
    def __init__(self, bank_id, bank_name):
        self.bank_id = bank_id
        self.bank_name = bank_name

    def show_detail(self):
        return f"Bank ID: {self.bank_id}, Bank Name: {self.bank_name}" 