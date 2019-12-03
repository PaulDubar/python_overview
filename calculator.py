num1 = float(input("Enter first number: ")) # convert input to float
oper = input("Enter operator: ")
num2 = float(input("Enter second number: ")) # convert input to float

if oper == '+':
    print(num1 + num2)
elif oper == '-':
    print(num1 - num2)
elif oper == '/':
    print(num1 / num2)
elif oper == '*':
    print(num1 * num2)
elif oper == '%':
    print(num1 % num2)
else:
    print("invalid operator!")
    