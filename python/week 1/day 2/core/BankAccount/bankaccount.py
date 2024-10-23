class BankAccount:
    balance=0
    int_rate=0.01
    def __init__(self, int_rate, balance): 
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