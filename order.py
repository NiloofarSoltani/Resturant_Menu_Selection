class Order:
    def __init__(self, customer):
        self.customer = customer
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)

    def view_cart(self):
        print(f"\n{self.customer}'s cart:")
        for item in self.cart:
            print(f"- {item.get_name()}: ${item.get_price():.2f}")

    def generate_bill(self):
        total_price = sum([item.get_price() for item in self.cart])
        print(f"\n{'*' * 30}")
        print(f"\n{self.customer}'s bill:\n")
        print(f"{'Item':<10} {'Price':>10}")
        print(f"{'-' * 20}")
        for item in self.cart:
            print(f"{item.get_name():<10} ${item.get_price():>10.2f}")
        print(f"\n{'Total':<10} ${total_price:>10.2f}")
        print(f"\n{'*' * 30}")

