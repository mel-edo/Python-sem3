# 1) WAP to find a number is prime or not
num = int(input())
flag = 0
if num < 2:
    flag = 1
for i in range(2, num):
    if num % i == 0:
        flag = 1
        break

if flag == 0:
    print(num, "is prime")
else:
    print(num, "is not prime")