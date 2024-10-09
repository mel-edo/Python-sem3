# 5) WAP that accepts strings and calculates the number of uppercase and lowercase letters in the string
str1 = input("Enter string: ")

upper, lower = 0, 0
for i in str1:
    if 97 <= ord(i) <= 122:
        lower += 1
    elif 65 <= ord(i) <= 90:
        upper += 1
print("Uppercase letters: ", upper, "\nLowercase letters: ", lower)