
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
        new_bal = amount_deposited + self.balance  # add deposited to existing bal in self
        charges = 5
        print('You new balance is ', new_bal - charges)
        # sms code
        print('SMS sent to ', self.phone)
        # you'll try withdraw.


# create an object from Account class
object =  Account('Jose',45454,22,555555,100,300)   # 100 is fee, 300 is default balance
# use above object to access its behv . i.e deposit
object.deposit(amount_deposited=2000)
# dot-notation above means you are accessing object behv






