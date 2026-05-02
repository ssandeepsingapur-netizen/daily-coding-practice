from abc import ABC, abstractmethod

# Encapsulation
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


# 🧬 Inheritance + 🎭 Polymorphism + 🧩 Abstraction
class Animal(ABC):   # Abstract class

    @abstractmethod
    def sound(self):   # Abstract method
        pass


class Dog(Animal):   # Inheritance
    def sound(self):  # Polymorphism (method overriding)
        print("Dog barks")


class Cat(Animal):   # Inheritance
    def sound(self):  # Polymorphism
        print("Cat meows")


# 🔹 Main Program
# Encapsulation usage
acc = BankAccount("Sandeep", 1000)
acc.deposit(500)
print("Balance:", acc.get_balance())

# Polymorphism usage
animals = [Dog(), Cat()]

for a in animals:
    a.sound()