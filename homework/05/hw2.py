class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return  ("Account owner   : {}".format(self.owner) + "\nAccount balance : {}".format(self.balance))

    def deposit(self, amount):
        self.balance += amount
        print ("Deposit Accepted")
    
    def withdraw(self, amount):
        if ( amount <= self.balance):
            self.balance -= amount
            print ("Withdrawal Accepted")
        else:
            print ("Funds Unavailable!")

acct1 = Account(owner='Alex', balance=100)

#print (acct1)
#print (acct1.owner)
#print (acct1.balance)

acct1.deposit(50)
print (acct1)
acct1.withdraw(75)
acct1.withdraw(500)
print (acct1)
