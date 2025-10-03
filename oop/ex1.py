
from abc import ABC, abstractmethod

# BankAccount Abstract Class
class BankAccount(ABC):
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass

    def display_balance(self):
        print(f"Balance : {self.balance} Baht.")

# SavingAccount extends BankAccount
class SavingAccount(BankAccount):
    def __init__(self, owner, balance):
        super().__init__(owner, balance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if (self.balance >= amount):
            self.balance = self.balance - amount

# CheckingAccount extends BankAccount
class CheckingAccount(BankAccount):
    def __init__(self, owner, balance):
        super().__init__(owner, balance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

# Main
somchai = SavingAccount("Somchai", 10000)
somsri = CheckingAccount("Somsri", 5000)

somchai.deposit(2000)
somsri.deposit(2000)

somchai.withdraw(8000)
somsri.withdraw(8000)

somchai.display_balance()
somsri.display_balance()
