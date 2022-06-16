class BankAccount:
    all_accounts = []

    def __init__(self, int_rate, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def display_all_bank_acc_infos(cls):
        for account in cls.all_accounts:
            print(f"Balance: ${account.balance}")
        

account1 = BankAccount(0.01)
account2 = BankAccount(0.03, 2000)

account1.deposit(1000).deposit(800).deposit(1500).withdraw(500.5).yield_interest().display_account_info()
account2.deposit(3000).deposit(650).withdraw(2000).withdraw(800).withdraw(1000).withdraw(500).yield_interest().display_account_info()

BankAccount.display_all_bank_acc_infos()