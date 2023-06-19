class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_animals(self):
        for animal in self.animals:
            print(f"{animal.name} says {animal.make_sound()}")

if __name__ == '__main__':
    zoo = Zoo()
    zoo.add_animal(Dog("Fido"))
    zoo.add_animal(Cat("Whiskers"))
    zoo.show_animals()