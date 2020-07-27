

# madam

x = 1
while x <=5:
    name = str(input('Enter Some Name: '))
    # reverse the string
    reverse = name[:: -1]  #  start, end , step
    print(reverse)

    if name == reverse:
        print('Its a palindrome')
        break
    else:
        print('Its not a palindrome')
        continue

    x = x + 1    # make x increment

