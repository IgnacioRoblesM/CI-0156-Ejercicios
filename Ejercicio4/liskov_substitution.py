from abc import ABC, abstractmethod


# This is the parent class
class Animal(ABC):
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def get_name(self):
        return self.name

    def get_sound(self):
        return self.sound

    @abstractmethod
    def make_sound(self):
        pass


# These are the child classes
class Lion(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)

    def make_sound(self):
        return "Roar!"


class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)

    def make_sound(self):
        return "Meow!"


class Cow(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)

    def make_sound(self):
        return "Moo!"


if __name__ == "__main__":
    lion = Lion("Lion", "Roar")
    cat = Cat("Cat", "Meow")
    cow = Cow("Cow", "Moo")
    animals = [lion, cat, cow]

    # This proves that I can replace a child class with a child class from the same parent
    for animal in animals:
        print(animal.make_sound())
