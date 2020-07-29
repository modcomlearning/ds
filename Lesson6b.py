
# functions with parameters
# Parameters are bits of information provided to functions, information can be a int, float, str, list

def my_shop(tax, name, money, balance): # tax, name, money, balance are params
    total = money - balance
    print('Your Available is ', total)
    # more logic
    print('The money available is ', money)
    print('The balance is ', balance)
    print('The tax is ', tax)
    print('Shop Keeper name is ', name)


# my_shop(tax=1.8, name='Jose')  # tax and name are arguments
my_shop(tax=2.5, name='Ann', money=4000, balance=200)
my_shop(tax=3.5, name='Tom', money=5000, balance=700)
my_shop(tax=4.5, name='Eunice', money=10000, balance=600)

