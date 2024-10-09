# 3) WAP to find the grade of student using given percentage
percentage = int(input())
if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 50:
    print("Grade D")
else:
    print("Grade F")