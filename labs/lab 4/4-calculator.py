# 4) WAP to create a simple console base calculator
print("Enter first number: ")
num1 = int(input())
print("Enter second number: ")
num2 = int(input())

while True:
    print("Enter +, -, /, *, %, //: ")
    operator = input()
    if operator == "+":
        print(num1 + num2)
        break
    elif operator == "-":
        print(num1 - num2)
        break
    elif operator == "*":
        print(num1 * num2)
        break
    elif operator == "/":
        print(num1 / num2)
        break
    elif operator == "//":
        print(num1 // num2)
        break
    elif operator == "%":
        print(num1 % num2)
        break
    else:
        print("Enter valid operator")