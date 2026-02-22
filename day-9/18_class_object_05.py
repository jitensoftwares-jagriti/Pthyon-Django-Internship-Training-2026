class BankAccount:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance

    def show_balance(self):
        print("Account Holder:", self.holder_name)
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)


# Creating an object
account = BankAccount("Jiten", 5000)

# Using methods
account.show_balance()
account.deposit(2000)
account.show_balance()
