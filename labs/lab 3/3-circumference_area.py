# 3) take radius from user and print circumference and area but take pi as const
from constant import pi
r = int(input("Enter radius: "))
area = pi * r**2
circumference = 2 * pi * r
print("area: ", area)
print("circumference: ", circumference)