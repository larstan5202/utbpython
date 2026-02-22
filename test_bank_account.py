from bank_account import BankAccount

def test_initial_balance_is_zero():
    account = BankAccount()
    assert account.balance() == 0

def test_deposit_adds_money():
    account = BankAccount()
    account.deposit(100)
    assert account.balance() == 100

def test_withdraw_removes_money():
    account = BankAccount()
    account.deposit(200)
    account.withdraw(50)
    assert account.balance() == 150

def test_withdraw_cannot_go_negative():
    account = BankAccount()
    account.deposit(50)
    account.withdraw(100)
    assert account.balance() == 50  # ingen övertrassering

def test_apply_interest_adds_interest():
    account = BankAccount()
    account.deposit(100)
    account.apply_interest(0.10)  # 10%
    assert account.balance() == 110

def test_can_pay_bill_true():
    account = BankAccount()
    account.deposit(300)
    assert account.can_pay_bill(200) is True

def test_can_pay_bill_false():
    account = BankAccount()
    account.deposit(100)
    assert account.can_pay_bill(200) is False