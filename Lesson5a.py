
# lists
# tuples
# functions  - intro

# ======Lists=======
# lists store multiple values in one variable
marks = [25,45,66,77,99,77,96.5, 45.56]
names = ['Jane','Halima','Tom']
# Lists uses []
# print in 2 ways
# manual way
print(marks[0])
print(names[2])
# automatically
for mark in marks:
    print(mark)

for name in names:
    print(name)
# slicing
print(marks[0:3])
print(marks[:4]) #  from start to number 4  , there is a minus one
print(marks[4:]) # from 4 and above

# UPDATE THE LIST
names.append('Anita')
names.remove('Tom')

for name in names:
    print(name)

# Lists are mutable/update



















