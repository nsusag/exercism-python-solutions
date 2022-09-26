OPEN = "open"
CLOSED = "closed"

class BankAccount:
    def __init__(self):
        self.balance = 0 
        self.status = CLOSED

    def get_balance(self):
        if self.status == CLOSED:
            raise ValueError("Cannot get the balance of a closed account.")
        return self.balance

    def open(self):
        if self.status == OPEN:
            raise ValueError("Cannot open an account that is already opened.")
        self.status = OPEN 

    def deposit(self, amount):
        if self.status == CLOSED:
            raise ValueError("Cannot deposit into a closed account.")
        if amount < 0:
            raise ValueError("Cannot deposit a negative amount.")
        self.balance += amount

    def withdraw(self, amount): 
        if self.status == CLOSED:
            raise ValueError("Cannot withdraw from a closed account.")
        if amount < 0:
            raise ValueError("Cannot withdraw a negative amount.")
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Cannot withdraw more money than is in the account.")

    def close(self):
        if self.status == CLOSED:
            raise ValueError("Cannot close an account that is already closed.")
        self.status = CLOSED 
        self.balance = 0
