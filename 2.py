class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance   # private

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(self.__balance)
acc1 = BankAccount("Sandeep", 1000)

print(acc1.deposit(500))
print(acc1.withdraw(200))
print("Balance:", acc1.get_balance())




