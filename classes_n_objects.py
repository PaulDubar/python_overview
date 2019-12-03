# Used to create your own data types in Python
# to store attributes about something more complex than a string or list can handle
# So an object can be used define a student datatype and its attributes
# A Class specifies an object type we want to define in Python
#
class Student:
    def __init__(self, name, major, gpa, is_on_probation): # initialise function within which we map the student attributes
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probabtion = is_on_probation