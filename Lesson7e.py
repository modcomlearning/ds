
from Lesson7d import payroll

returned_gross = payroll(basic=5000, allowances=500)

# check if gross is less than  6000
print(returned_gross)

if returned_gross > 10000:
    print('Get 50% discount')
else:
    print('Get 25% Discount')

