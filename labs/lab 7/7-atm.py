class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return f"Your balance is: Rs{self.balance:.2f}"

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        self.balance += amount
        return f"Successfully deposited Rs{amount:.2f}. {self.check_balance()}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Successfully withdrew Rs{amount:.2f}. {self.check_balance()}"

    def transfer(self, amount, other_account):
        if amount <= 0:
            return "Transfer amount must be positive."
        if amount > self.balance:
            return "Insufficient funds for transfer."
        self.balance -= amount
        other_account.balance += amount
        return f"Successfully transferred Rs{amount:.2f}. {self.check_balance()}"

my_account = ATM(1000)
other_account = ATM(500)

print(my_account.check_balance())
print(my_account.deposit(200))
print(my_account.withdraw(150))
print(my_account.transfer(100, other_account))
print(other_account.check_balance())
