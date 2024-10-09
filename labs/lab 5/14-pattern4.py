# 14) pattern:
'''
*****
****
***
**
*'''
n = int(input())
for i in range(n + 1, 0,  -1):
    for j in range(i + 1, 2, -1):
        print("*", end=" ")
    print()