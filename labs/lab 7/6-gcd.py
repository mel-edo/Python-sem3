# 6) WAP to compute GCD of 2 numbers
num1 = int(input("Num1: "))
num2 = int(input("Num2: "))

for i in range(min(num1, num2), 0, -1):
    if num1 % i == 0 and num2 % i == 0:
        print(i, "is the GCD of", num1, "and", num2)
        break