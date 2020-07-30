
# Lets create a function with parameters and returns a value

def payroll(basic, allowances):
    print('Basic is ', basic)
    print('Allowances is ', allowances)
    gross = basic + allowances
    print('Your gross is ', gross)
    return gross


# call/use/
# NB: payroll has parameters and it returns
returned_gross = payroll(basic=30000, allowances=2000)
print('Your Gross Salary is ', returned_gross, 'KES')



