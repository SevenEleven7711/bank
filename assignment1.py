
class BankAccount:
    def __init__(self, customer_id, name, starting_balance=0):
        self.customer_id = customer_id
        self.name = name
        self.balance = starting_balance
        self.transactions = {}  # Dictionary to record transactions

    def print_account_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Balance: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions[f"deposit"] = amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transactions[f"withdrawal"] = amount
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds for withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def print_transactions(self):
        if not self.transactions:
            print("No transactions recorded.")
            return
        for transaction, amount in self.transactions.items():
            print(f"{transaction}: ${amount:.2f}")

