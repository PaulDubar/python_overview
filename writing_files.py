# this follows on from reading_files.py
# uses employees.txt

print("Now using employees.txt with append mode")
try:
    employee_file = open("employees.txt", "a") # w is write only, a is append, r+ is read/write
except FileNotFoundError as no_file_found:
    print(no_file_found)
employee_file.write("\nToby - HR") # add newline with \n
employee_file.close()

print("Now using employees.txt with w - write - this overwrites the entire file")
try:
    employee_file = open("employees.txt", "w") # w is write only, a is append, r+ is read/write
except FileNotFoundError as no_file_found:
    print(no_file_found)
employee_file.write("Toby - HR") # Don't need \n to start line1
print("The entire file is overwritten with one line only")
employee_file.close()

# So can use w mode to create a new file. E.g. a web page
