from object_class_functions import Student
#create two student objects
student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Phyllis", "Business", 3.8)

# ask the object if the student is on the honour roll
# this calls the function in the object class for the given student
print(student1.on_honour_roll()) # we need the parentheses because its a function call
print(student2.on_honour_roll()) 

# basically a class function provides a service to the objects of a class