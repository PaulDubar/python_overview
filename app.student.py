# uses class defined in the classes_n_objects.py
# create a student object 
from classes_n_objects import Student
student1 = Student("Paul","Psychology",3.1,False) # instantiate an object called student1
# what happens is the values you provide for the object are passed to the class and the init function
# assigns each value to the attribute of the Student object type
print(student1.name)