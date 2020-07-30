
# Using return in functions

def addition(): # without parameters
    x = 8
    y = 6
    answer = x + y
    #print('Your Total is ', answer)
    if answer > 5:
        return x
    else:
        return y

# you are asked to use the answer in line 13 below
returned_answer = addition()
# here
print('Answer is ', returned_answer)
# above answer/result from the the functions,  can now be used outside the function
print(type(returned_answer))



