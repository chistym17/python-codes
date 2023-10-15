class bank:
    def __init__(self,balance):
        self.balance=balance

    def add_money(self,amount):
        if amount>0 :
            self.balance+=amount
            print(f'amount added.new balance{self.balance}')
        else:
            print("invalid amount")
    
    
    def withdraw_money(self,money):
        if money<=10 or money>=500000:
            print("withdrawal limit reached.Enter a new amount")
        else:
            self.balance-=money
            print(f'amount{money}deducted . New balance{self.balance}')
    
    def check_balance(self):
        print(self.balance)



     
brac=bank(10000)
brac.add_money(2000)
print("\n")
brac.withdraw_money(4000)

