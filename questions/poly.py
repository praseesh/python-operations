class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number  # private attribute
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

# Creating an instance of BankAccount
account = BankAccount("123456", 1000)

# Accessing private attributes and methods using public methods
print("Account Number:", account.get_account_number())  # Output: Account Number: 123456
print("Current Balance:", account.get_balance())  # Output: Current Balance: 1000


account.deposit(500)  # Output: Deposited $500. New balance: $1500
account.withdraw(200)  
account.withdraw(2000)  
