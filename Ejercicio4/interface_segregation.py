from abc import ABC, abstractmethod


# Ability to make a call
class Phone(ABC):
    def __init__(self, number):
        self.number = number

    @abstractmethod
    def make_call(self):
        pass


# Ability to take a picture
class Camera(ABC):
    def __init__(self):
        """This class needs has no attributes"""
        pass

    @abstractmethod
    def take_picture(self):
        pass


# Ability to play a game
class Game(ABC):
    def __init__(self, game_name):
        self.game_name = game_name

    @abstractmethod
    def play_game(self):
        pass


# This class has all the abilities
class IPhone(Phone, Camera, Game):
    def __init__(self, number, game_name):
        Phone.__init__(self, number)
        Camera.__init__(self)
        Game.__init__(self, game_name)

    def make_call(self):
        return f"Calling {self.number}..."

    def take_picture(self):
        return "Taking picture..."

    def play_game(self):
        return f"Playing {self.game_name}..."


# This class has only the ability to make a call
class Nokia(Phone):
    def __init__(self, number):
        Phone.__init__(self, number)

    def make_call(self):
        return f"Calling {self.number}..."
