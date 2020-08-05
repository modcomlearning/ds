
# create a bank account class
# for account to be an object, we need attr, behv
class Account:
    def __init__(self, name, accno, age, phone, fee, balance):
        self.name = name
        self.accno = accno
        self.fee = fee
        self.phone = phone
        self.balance = balance

    def deposit(self, amount_deposited):
        self.balance = amount_deposited + self.balance  # add deposited to existing bal in self
        charges = 5
        print('You new balance is after deposit: ', self.balance - charges)
        # sms code
        print('SMS sent to ', self.phone)
        # you'll try withdraw.


    def withdraw(self, withdrawn_amount):
        self.balance = self.balance - withdrawn_amount
        # more logic here
        print('You withdrew ', withdrawn_amount)
        print('Your balance is ', self.balance)

# create an object from Account class
x =  Account('Jose',45454,22,729225710,100,300)   # 100 is fee, 300 is default balance
# use above object to access its behv . i.e deposit
x.deposit(amount_deposited=2000)
x.withdraw(withdrawn_amount=3000)
# dot-notation above means you are accessing object behv
# Object should function, they should have functions
print(type(x))






