class Account:

    @staticmethod
    def Welcome():
        print("Welcome to account")
    def __init__(self,bal,acc):
        self.bal = bal
        self.acc = acc
    
    def debit(self,ammount):
        self.bal-=ammount
        print(f"Rs {ammount} is debited from your Account")
        print("total Balance Is:", self.get_balance())
    
    def credit(self,ammount):
        self.bal+=ammount
        print(f"Rs {ammount} credited to your account")
        print("total Balance Is:", self.get_balance())


    def get_balance(self):
        return self.bal
    
    def showBalanceAndAccountNo(self):
        print(f"AccNo: {self.acc}")
        print(f"your Current Balance Is {self.bal}")


cust1 = Account(70000,"123456bhiu")
cust1.Welcome()
print(cust1)
print(cust1.debit(1000))
print(cust1.credit(1000))



        
    
