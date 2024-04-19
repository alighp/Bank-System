class Branch:
    def __init__(self, bank_id, branch_id, branch_name, number_of_customers, budget, city):
        self.bank_id = bank_id
        self.branch_id = branch_id 
        self.branch_name = branch_name
        self.number_of_customers = number_of_customers
        self.budget = budget
        self.city = city

    def show_detail(self):
        return f"Branch ID: {self.branch_id}\
        Branch Name: {self.branch_name}\
        Number of customers: {self.number_of_customers}\
        Budget: {self.budget}\
        City: {self.city}" 

