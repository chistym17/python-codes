class user:
    users=[]
    __total_balance=0
    __total_loan=0
    def __init__(self,name,email,password,amount) -> None:
        self.name=name
        self.email=email  
        self.password=password
        self.balance=amount
        self.users.append(name)
        self.transaction_history=[]
        user.__total_balance+=amount
    
    def deposit(self,amount):
        self.balance+=amount
        self.transaction_history.append(f"deposited : {amount}")
        user.__total_balance+=amount



    def withdraw(self,amount):
        if amount<=0 or amount>self.balance:
            print("Invalid Amount.")
        else:
            self.balance-=amount
            self.transaction_history.append(f"withdrawed: {amount}")
            user.__total_balance-=amount



    def transfer_money(self,receipent,amount):
        if receipent.name not in self.users:
            print("No account found")
        elif amount>self.balance or self.balance==0:
            print("Not enough balance")
        else:
            self.balance-+amount
            receipent.deposit(amount)
            self.transaction_history.append(f"transfered: {amount}")


    def take_loan(self,admin,amount):
        if admin.loan_permission(self) is False:
            print("Sorry.Loan denied")

        if amount>self.balance*2:
            print("Max loan limit reached")

        else:
            print(f"Here is your loan-{amount}")
            self.transaction_history.append(f"loan taken: {amount}")
            user.__total_loan+=amount

    def show_transactions(self):
        print("All previous transactions : ")
        return self.transaction_history
    
    def check_balance(self):
        return f"Current balance of {self.name}: {self.balance}"
    
    @staticmethod
    def show_total_balance(admin):
        if isinstance(admin,Admin):
            return user.__total_balance
        else:
            print("Acess denied")

      
    @staticmethod
    def show_total_loan(admin):
        if isinstance(admin,Admin):
            return user.__total_loan
        else:
            print("Acess denied")


class Admin:
    def __init__(self,name,password) -> None:
        self.name=name
        self.password=password

    def loan_permission(self,user):
        if user.show_total_balance()<user.show_total_loan():
            return False
        else:
            return True






# Example usage:
user1 = user("John", "john@example.com", "password123",2000)
user2 = user("Alice", "alice@example.com", "password456",400)


# Deposit and withdraw
user1.deposit(500)
user1.withdraw(200)

# Transfer money
user1.transfer_money(user2, 300)

# Check balance
print(user1.check_balance())
print(user2.check_balance())

# Take a loan
user1.take_loan(1500,Admin)

# Get transaction history
print(user1.show_transactions())
print(user2.show_transactions())