# reading text files or csv from the operating system
# uses employees.txt
print("Block 1 deliberately shows how to trap an error - the file doesnt exist")
try:
    employee_file = open("employees.csv", "r") # w is write only, a is append, r+ is read/write
except FileNotFoundError as no_file_found:
    print(no_file_found)

print("Block 2 is where the file exists")
print("employee_file variable is a pointer to the content of the opened file")
try:
    employee_file = open("employees.txt", "r") 
except FileNotFoundError as no_file_found:
    print(no_file_found)
# always insert a close file before coding your block so you dont forget
print(employee_file.readable()) # function returns True if file is readable
print(employee_file.readline()) # function to print current line. multiple executions prints all content
print(employee_file.read()) # function to print all the contents from current line
print("Only 4 lines got printed because file pointer had already printed line one in previous command")

employee_file.close()

print("Now lets re-open the file and read its content into a list")

try:
    employee_file = open("employees.txt", "r") 
except FileNotFoundError as no_file_found:
    print(no_file_found)
# always insert a close file before coding your block so you dont forget
print(employee_file.readable()) # function returns True if file is readable
print(employee_file.readlines()) # function to read content into a list
# output is a list like
# 'Jim - Salesman\n', 'Dwight - Salesman\n', 'Pam - Receptionist\n', 'Michael - Manager\n', 'Oscar - Accountant']
# There is a newline, just like in the text file itself
employee_file.close()

# Now access the list element by element number

print("re-open the file to access the list elements by element number using readlines()[0]")
employee_file = open("employees.txt", "r")
print(employee_file.readlines()[0]) # print element 0 in list 
employee_file.close()
#
print("Now lets loop through the file in a for loop instead")
employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee) 
employee_file.close()