class BankAccount: 
    

    def __init__(self, balance):
        self.balance = balance

    def add_money(self, amount):
        self.balance += amount

    def subtract_money(self, amount):
        self.balance -= amount
        print(f"Withdrawal for {amount} successful, remaing balance: {self.balance}")
        

class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):

        super().__init__(balance)
        self.min_balance = min_balance

    def subtract_money(self, amount):
        
        if (self.balance - amount) < self.min_balance:
            print(f"unable to withdraw funds, remaining balance less than {self.min_balance}. Remaining balance of {self.balance}.")
        else:
            return super().subtract_money(amount)
        

account= SavingsAccount (1500,500)

print (f"The account balance {account.balance}")

account.subtract_money(300)

account.subtract_money(600)

account.subtract_money(500)




