
# Parrot
# for my program to form an object
# it must have atrributes, behaviors
class Parrot:
    # below defines parrot attributes
    def __init__(self, name, age, color):
        self.name = name # name is now in self
        self.age = age

    def singing(self, song2): # behaviors are functions
        song = 'Jingle Bells'
        print('Its singing..', song, 'and', song2)
        print('Its name is ', self.name)  # behv using an attribute

    def dancing(self):
        print(self.name, 'Is dancing')
        print(self.name, 'is ', self.age, 'Yrs old')


# the class creates the object
object = Parrot("Woo",2,"White")
# use above object to access the bahv of the parrot
object.singing("Row row your boat")
object.dancing()



















