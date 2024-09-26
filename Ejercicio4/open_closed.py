from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, salute):
        self.name = name
        self.salute = salute

    def get_name(self):
        return self.name

    def get_salute(self):
        return self.salute

    # This method can be expanded by child classes
    @abstractmethod
    def say_hi(self):
        pass


class Mechanic(Employee):
    def __init__(self, name, salute):
        super().__init__(name, salute)

    def say_hi(self):
        return "Hi, I love fixing cars!"


class Accountant(Employee):
    def __init__(self, name, salute):
        super().__init__(name, salute)

    def say_hi(self):
        return "Hi, I love numbers!"


class Teacher(Employee):
    def __init__(self, name, salute):
        super().__init__(name, salute)

    def say_hi(self):
        return "Hi, I love to teach!"
