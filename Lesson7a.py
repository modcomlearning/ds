
# question 1 with paramters
def check_number(x):
    # x  = 5
    if x > 0:
        print('Pos')
    elif x < 0:
        print('Neg')
    else:
        print('Its zero')


# call/invoke/trigger/use
check_number(x=8)

# QUESTION 2 , GIVEN 3 Variables , check the largest
def check_largest():
    x = 5
    y = 5
    z = 5

    if x > y and x > z:
        print('X is the Largest')

    elif y > x and y > z:
        print('Y is the largest')

    elif z > x and z > y:
        print('Z is the largest')

    else:
        print('They must be equal')


# call/use
check_largest()









