name = input("Enter your name: ")
print("Hello " + name + "!")
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)
print(result)
# But the above only works for integers.
# An error occurs if you input non-integers
num3 = input("Enter a number: ")
num4 = input("Enter another number: ")
result2 = float(num3) + float(num4)
print(result2)