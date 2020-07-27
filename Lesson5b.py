
# tuple
# Store multiple values in one variable
points = (500,450,560.5,789,456,200)
names = ('John','Hassan','Jane','Clare')
# tuple use ()

# manual way
print(points[1])
print(names[2])

# automatic way
for point in points:
    print(point)

# sliced
print(points[2:5])  # from 2 to 5th item , always a minus 1
print(points[:4])  # from start to 4
print(points[4:])  # from 4 and above

# update tuples
#$ tuples are immutable , cannot be updated
# names.append('Joseph')

# In conclusion, Lists are mutable(can be updated) and tuples are immutable (can't be updated)


