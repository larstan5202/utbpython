class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount

    def balance(self):
        return self._balance

    def apply_interest(self, rate):
        # rate t.ex. 0.05 för 5%
        if rate > 0:
            self._balance += self._balance * rate

    def can_pay_bill(self, amount):
        return amount <= self._balance