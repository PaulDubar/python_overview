# Classes are used to create your own data types in Python
# to store attributes about something more complex than a string or list can handle
# So an object can be used to define a student datatype and its attributes
# A Class specifies an object type we want to define in Python
#
# This class file is used by app2_student.py program
#
class Student:
    def __init__(self, name, major, gpa): # initialise function within which we map the student attributes
        self.name = name
        self.major = major
        self.gpa = gpa

# we can also define functions within a class that can be used by objects of the class
# in doing so, any student object created from this class can access the function
# basically a class function provides a service to the objects of a class

# lets create a function to tell us if a student is on the honour roll
    def on_honour_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
