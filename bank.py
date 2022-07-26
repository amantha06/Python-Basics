class Account():
    def __init__(self, owner, balence):
        self.owner = owner
        self.balence = balence
    
    def deposit(self,depo):
        bal = depo + self.balence
        return bal
    
        print("please enter an integer")

    def withdraw(self, withd):
        if withd > self.balence:
            print(self.owner + " you do not have that much money to withdraw :( ")
        else:
            bal = self.balence - withd
            return bal
        
            

myaccount = Account("Anirudh", 10000)
print(myaccount.owner)
print(myaccount.balence)

print(myaccount.deposit(100))
print(myaccount.withdraw(100000))
