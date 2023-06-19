class Bill:
    def __init__(self, customer):
        self.customer = customer

    def generate_bill(self):
        self.customer.generate_bill()
