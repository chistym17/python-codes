class base_account:
    def __init__(self,acc_number,balance) -> None:
        self._acc_number=acc_number
        self._balance=balance
    
    def deposit(self,amount):
        if amount<=0:
            print ("invalid amount")
        else:
            self.balance+=amount
    def withdraw(self,amount):
             if amount<=0:
               print ("invalid amount")
             else:
              self.balance-=amount
    def show_balance(self):
        print(f'Your current balance is : {self._balance}')
    

class savings_account(base_account):
    interest_rate=.05

    def __init__(self, acc_number, balance) -> None:
        super().__init__(acc_number, balance)
    

    def _calculate_interest(self):
        interest=self.balance*self.interest_rate
        self.balance=self.balance+interest
        return self.balance

    def deposit(self, amount):
                self.balance=self._calculate_interest(self)
                return super().deposit(amount)
        

class checking_account(base_account):
     overdraft_limit=2500
     def __init__(self, acc_number, balance) -> None:
          super().__init__(acc_number, balance)
     def withdraw(self, amount):
          if self._balance+self.overdraft_limit<amount:
               print("sorry.overdraft limit exists")
          else:
           return super().withdraw(amount)

class investment_account(base_account):
     def __init__(self, acc_number, balance,risk_level) -> None:
          self.risk_level=risk_level
          super().__init__(acc_number, balance)
     def update_risk_level(self,new_risk_level):
                self.risk_level = new_risk_level
     def current_risk_level(self):
          return self.risk_level
                

          





mrm=savings_account("1245",5000)
mrm.show_balance()
mrm.deposit(400)
mrm.show_balance()
print(mrm._acc_number)
