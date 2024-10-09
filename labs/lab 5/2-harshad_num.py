# 2) WAP to det whether the given number is a harshad number (if number is divisible by the sum of its digits, then its harshad number)
num = input()
sum = 0
for i in num:
    sum += int(i)
if int(num) % sum == 0:
    print(num, "is harshad number")
else:
    print(num, "is not a harshad number")