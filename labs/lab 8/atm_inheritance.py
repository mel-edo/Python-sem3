'''
Basic bank functions with inheritance
- create a base class called account with attributes like account no., account holder name, balance
- define methods such as check balance, deposit, withdraw
- extend account into specialized classes like savings account, current account and checking account
How could you modify the withdraw method in these subclasses to handle withdraw limits for each account type

- Add a transaction history class that maintains a record of all deposits and withdrawals for an account
- In this class implement a show_history method to display the transactions
'''
class TransactionHistory:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction_type, amount):
        transaction = {"type": transaction_type, "amount": amount}
        self.transactions.append(transaction)

    def show_history(self):
        if not self.transactions:
            print("No transactions yet.")
            return
        print("Transaction History:")
        for transaction in self.transactions:
            print(f"{transaction['type']}: {transaction['amount']}")


class Account:
    def __init__(self, account_no, account_holder_name, balance=0):
        self.account_no = account_no
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.transaction_history = TransactionHistory()
    
    def check_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.add_transaction("Deposit", amount)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print("Insufficient funds.")
            return False
        self.balance -= amount
        self.transaction_history.add_transaction("Withdrawal", amount)
        return True

    def show_history(self):
        self.transaction_history.show_history()


class SavingsAccount(Account):
    def __init__(self, account_no, account_holder_name, balance=0, withdrawal_limit=3):
        super().__init__(account_no, account_holder_name, balance)
        self.withdrawal_limit = withdrawal_limit
        self.withdrawals_made = 0

    def withdraw(self, amount):
        if self.withdrawals_made >= self.withdrawal_limit:
            print(f"Withdrawal limit reached. You can only withdraw {self.withdrawal_limit} times per month.")
            return False
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print("Insufficient funds.")
            return False
        self.balance -= amount
        self.withdrawals_made += 1
        self.transaction_history.add_transaction("Withdrawal", amount)
        return True


class CurrentAccount(Account):
    def __init__(self, account_no, account_holder_name, balance=0, overdraft_limit=500):
        super().__init__(account_no, account_holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > (self.balance + self.overdraft_limit):
            print("Exceeded overdraft limit. Insufficient funds.")
            return False
        self.balance -= amount
        self.transaction_history.add_transaction("Withdrawal", amount)
        return True


class CheckingAccount(Account):
    def __init__(self, account_no, account_holder_name, balance=0, transaction_fee=2):
        super().__init__(account_no, account_holder_name, balance)
        self.transaction_fee = transaction_fee
        self.transactions_made = 0
        self.transaction_limit = 20

    def withdraw(self, amount):
        if self.transactions_made >= self.transaction_limit:
            print(f"Transaction limit reached. You have made {self.transactions_made} transactions this month.")
            return False
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print("Insufficient funds.")
            return False
        self.balance -= (amount + self.transaction_fee)
        self.transactions_made += 1
        self.transaction_history.add_transaction("Withdrawal", amount)
        return True


savings_account = SavingsAccount(101, "Alice", balance=1000)
current_account = CurrentAccount(102, "Bob", balance=500)
checking_account = CheckingAccount(103, "Charlie", balance=300)

print("Savings Account:")
savings_account.deposit(500)
savings_account.withdraw(200)
savings_account.withdraw(100)
savings_account.show_history()

print("\nCurrent Account:")
current_account.deposit(200)
current_account.withdraw(600)
current_account.show_history()

print("\nChecking Account:")
checking_account.deposit(100)
checking_account.withdraw(50)
checking_account.show_history()
