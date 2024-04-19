from src.Entities.person import Person

class Customer(Person):
    def __init__(self, branch_id, customer_id, first_name, last_name, national_code, address):
        super().__init__(first_name, last_name)
        self.branch_id = branch_id
        self.customer_id = customer_id
        self.national_code = national_code
        self.address = address

