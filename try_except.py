# This is how to catch errors in Python
number = int(input("Enter a number: ")) # if you don't enter an int, an error will occur
print(number) 

# Error per below is thrown if non int is input
# Enter a number: fred
# Traceback (most recent call last):
#  File "/Volumes/Data/Documents/Training/Coding/Python/try_except.py", line 2, in <module>
#    number = int(input("Enter a number: ")) # if you don't enter an int, an error will occur
# ValueError: invalid literal for int() with base 10: 'fred'
#
# a try except block allows the program to deal with errors
try:
    number = int(input("Enter a number: ")) # if you don't enter an int, an error will occur
    print(number)
except: 
    print("Invalid Input") # basically if any error occurs in try block, we run this
#
# Enter a number: fred
# Invalid Input
#
# However, the except is too broad and will print the same thing for any type of error
# example below throws invalid input for the divide by zero, and we dont even input anything
#
print ("Now enterting the 10/0 code block")
try:
    value = 10/0
    number = int(input("Enter a number: ")) 
    print(number)
except: 
    print("Invalid Input") 
#
# Invalid Input is thrown immediately due to the 10/0
#
# We can catch different types of exceptions with the except
#
print("Now entering how to use two different except blocks code sample")
try:
    value = 10/0 # comment this line to test the next code line
    number = int(input("Enter a number: ")) 
    print(number)
except ZeroDivisionError: 
    print("Divided by zero") 
except ValueError:
    print("Invalid input")
#
# rather than printing your own error message, you can print pythons internal error
# 
print("Now printing pythons internal error code block") 
try:
    value = 10/0 # comment this line to test the next code line
    number = int(input("Enter a number: ")) 
    print(number)
except ZeroDivisionError as err: 
    print(err)  # print out the error thrown
except ValueError as value_err: 
    print(value_err) # if i entered a float not an int, python displays internal error

# Best practise in Python is to catch specific errors - derrr.