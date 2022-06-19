class BankAccount:
    all_accounts = []

    def __init__(self, int_rate, account_name, balance=0): 
        self.int_rate = int_rate
        self.account_name = account_name
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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount.all_accounts

    def make_deposit(self, account, amount):
        for acc in self.account:
            if acc == account:
                acc.deposit(amount)

    def make_withdraw(self, account, amount):
        for acc in self.account:
            if acc == account:
                acc.withdraw(amount)

    def display_user_balance(self, account):
        for acc in self.account:
            if acc == account:
                print(f"User: {self.name}, {acc.account_name} Balance: {acc.balance}")

    def transfer_money(self, sender_account, receiver_account, amount, other_user):
        for acc in self.account:
            if acc == sender_account:
                acc.balance -= amount
                for transfer_acc in other_user.account:
                    if transfer_acc == receiver_account:
                        transfer_acc.balance += amount


account1 = BankAccount(0.01, "Checking")
account2 = BankAccount(0.03, "Saving", 2000)
account3 = BankAccount(0.02, "Checking")

first_user = User("Ada", "alovelace@codingdojo.com")
first_user.make_deposit(account1, 1000)
first_user.make_deposit(account2, 500)

second_user =  User("Anne", "abill@codingdojo.com")
second_user.make_deposit(account3, 50)

first_user.transfer_money(account1, account3, 600, second_user)


first_user.display_user_balance(account1)
first_user.display_user_balance(account2)
second_user.display_user_balance(account3)

