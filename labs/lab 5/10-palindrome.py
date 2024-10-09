# 10) WAP to check whether a given number is palindrome or not
num = input()
if num == num[::-1]:
    print(int(num), "is a palindrome")
else:
    print(int(num), "is not a palindrome")