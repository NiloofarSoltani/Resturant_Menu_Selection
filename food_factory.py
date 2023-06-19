from burger import Burger
from pizza import Pizza
from pepsi import Pepsi
from water import Water


class FoodFactory:
    def get_food(food: str):
        foods = {'burger': Burger(), 'pizza': Pizza(), 'pepsi': Pepsi(), 'water': Water()}
        return foods[food]
