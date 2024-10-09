# wap to perform addition, subtraction, multiplication, division on two floating point number and print the result upto two places of decimal
a = float(input("first float: "))
b = float(input("second float: "))
print(round(a + b, 2))
print(round(a - b, 2))
print(round(a * b, 2))
print(round(a / b, 2))
# can be done as print(f"Result: {result: .2f}")
# print("result: %.2f" % result)