class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initial_amount, acctName):
        self.name = acctName
        self.balance = initial_amount
        print(f"\nAccount name: '{acctName}' created.\nBalance: {self.balance:.2f}₪")

    def get_balance(self):
        print(f"\nAccount '{self.name}' Balance= {self.balance:.2f}₪")

    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposit Complete")
        self.get_balance()
        print(f"added {amount}₪")

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"Sorry, account '{self.name}' only has a balance of {self.balance:.2f}₪ ")

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            self.get_balance()
            print(f"Withdraw Complete")
            print(f"Withdraw {amount}₪")
        except BalanceException as error:
            print(f"\n Withdraw Error: {error}")

    def transfer(self, amount, account):
        try:
            print("\n*********\n\nBeginning Transfer 🚀🚀🚀 ")
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\n Transfer Complete! ✅ ")
            account.get_balance()
            self.get_balance()
        except BalanceException as error:
            print(f"\nTransfer Error ❎: {error}")


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("Deposit Complete")
        self.get_balance()


class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, acct_name):
        super().__init__(initial_amount, acct_name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("Withdraw Complete")
            self.get_balance()
        except BalanceException as error:
            print(f"\n Withdraw Interrupted: {error}")
