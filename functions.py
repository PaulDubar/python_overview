# function to say hello to the user
def hello(user, years):
    print("Hello " + user + " you are " + years + " old")

name = input("Enter your name: ")
age = input("How old are you:? ")
# passed parameters are positional and dont need to be named the same in the called function
hello(name, age) 
#
# Return statement in functions return a value
#
def cube(num):
    return num * num * num # return must be last statement in a function

# call the function passing in 3. Without print, youd see no output
print(cube(3))

result=(cube(4)) # store the result in variable
print(result) # print the variable



    