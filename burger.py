from food import Food

class Burger(Food):
    def __init__(self):
        super().__init__("Burger", 5.99)