class BankAccount:
    def __init__(self,int_rate=0.01, balance=0): 
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance=self.balance +amount
        return self
    def withdraw(self, amount):
        if self.balance<amount :
            print ("Insufficient funds: Charging a $5 fee")
            self.balance=self.balance-5
        else :
            self.balance=self.balance- amount
        return self    
    def display_account_info(self):
        print(f"Balance :${self.balance}") 
        return self
    def yield_interest(self):
        if self.balance>0 :
            self.balance=self.balance + (self.balance*self.int_rate)
        return self
AlexUser=BankAccount(0.2,250)
SmithUser=BankAccount(0.1,150)
AlexUser.deposit(150).deposit(80).deposit(280).withdraw(300).yield_interest().display_account_info()
SmithUser.deposit(650).deposit(520).withdraw(100).withdraw(50).withdraw(200).withdraw(150).yield_interest().display_account_info()
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self, amount):
        self.account.balance=self.account.balance + amount
        print(self.account.balance)
    def make_withdrawal(self, amount):
        if self.account.balance<amount :
            print ("Insufficient funds: Charging a $5 fee")
            self.account.balance=self.balance-5
        else :
            self.account.balance=self.account.balance- amount
        return self    
    def display_user_balance(self):
        print(f"The User :{self.name} has in his account the balence of:$ {self.account.balance}")        
NewUser=User("ali","aliii")
NewUser.display_user_balance()
NewUser.make_deposit(100)
NewUser.make_withdrawal(30)
NewUser.display_user_balance()