# 1) WAP to check if given number is disarium number (1^1 + 7^2 + 5^3 = 175)
num = input()
sum = 0
count = 1
for i in num:
    sum += int(i)**count
    count += 1
if sum == int(num):
    print(num, "is a disarium number")
else:
    print(num, "is not a disarium number")
