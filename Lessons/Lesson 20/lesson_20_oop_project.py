from bank_accounts import *

Tavor = BankAccount(1000,"Tavor")
Dave = BankAccount(2000,"Dave")
Dave.get_balance()
Tavor.get_balance()

Tavor.deposit(3000)
Dave.deposit(200)
Tavor.withdraw(1000000)
Dave.withdraw(10)

Dave.transfer(100,Tavor)

Ehud= InterestRewardsAcct(1000,"Ehud")
Ehud.get_balance()
Ehud.deposit(100)
Ehud.transfer(100,Tavor)

David = SavingsAcct(1000,"David")
David.get_balance()
David.withdraw(100)
David.transfer(10000,Tavor)