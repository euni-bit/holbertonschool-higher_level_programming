from abc import ABC

class Animal(ABC):
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class cat(Animal):
    def sound(self):
        return "Meow"
