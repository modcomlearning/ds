

password = str(input('Enter Your Password:'))
# string functions
import re
if len(password) < 8:
    print('Your Password is too short')

elif password.startswith('qwe') or password.startswith('1234'):
    print('password not accepted')

elif password.islower():
    print('Lowercase not accepted')

elif password.isdigit():
    print('Digits only not accepted')

elif password.endswith('1'):
    print('You cannot end with a 1')

elif not re.search("[!@#$&*_+=]", password):
    print('Not found  a symbol')

else:
    print('Right Password!')