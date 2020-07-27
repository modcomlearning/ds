
# Dictionary, Updatable/mutable
# Its uses key/value

student = {
    'name': 'Joseph',
    'gender': 'Male',
    'id': 45454545,
    'fee':450.50,
    'town': 'Thika'
}


print(type(student))
# use keys to pull out data in dictionary
print(student['gender']) # method 1
print(student.get('town')) # method 2

# lets update town
student['town']  = 'Lavington'
student['fee'] = 500
# repeat the print
print(student)




