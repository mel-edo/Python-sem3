# 2) WAP to find the given number is palindrome or not
num = int(input())
num = str(num)
if num == num[::-1]:
    print(int(num), "is a palindrome")
else:
    print(int(num), "is not a palindrome")