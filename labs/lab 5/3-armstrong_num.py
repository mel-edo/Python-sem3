# 3) WAP to print armstrong number from 1 to 1000
num = 1
while num < 1000:
    sum = 0
    for i in str(num):
        sum += int(i)**len(str(num))
    if sum == num:
        print(num)
    num += 1
