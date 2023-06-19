import food_factory
from food_factory import FoodFactory
from customer import Customer
from bill import Bill
from order import Order
from customer2 import Customer2

print("Hello User")
name = input("What is your name?")
customer = Customer2(name)

print("Welcome to our restaurant! Please choose your items from the menu below after finished enter 5. Done:\n")
print("1. Burger - $5.99")
print("2. Pizza - $8.99")
print("3. Pepsi - $1.99")
print("4. Water - $0.99")
print("5. Done")

choices = {1: 'burger', 2: 'pizza', 3: 'pepsi', 4: 'water'}
order = Order(customer)
while True:
    choice = int(input("\nEnter your choice: "))
    if choice in choices.keys():
        order.add_to_cart(FoodFactory.get_food(choices[choice]))
    elif choice == 0:
        break
    else:
        print("Invalid choice, please try again.")

# john.view_cart()
# bill = Bill(john)
# bill.generate_bill()


order.view_cart()
order.generate_bill()
