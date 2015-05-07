# calculator.py


print ( "Hi")
a = input("Enter number for a: ")
a = int(a)
b = input("Enter number for b: ")
b = int (b)
oper = input("Enter operator. Choose from +, -, *, и /: ")

if oper == "+":
    print (a + b)
elif oper == "-":
    print (a - b)
elif oper == "*":
    print (a * b)
elif oper == "/":
    print (a / b)
else:
    print ( "Invalid operator")

