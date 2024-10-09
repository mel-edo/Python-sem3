# 9) WAP to check whether the given number is perfect or not
# perfect number is a number which is equal to sum of its positive proper divisors
num = int(input())
divisors = [1]
for i in range(2, num):
    if num % i == 0:
        divisors.append(i)
if num == sum(divisors):
    print(num, "is a perfect number")