# 15) pattern:
'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1'''
n = int(input())
for i in range(n + 1, 0,  -1):
    for j in range(2, i + 1):
        print(j - 1, end=" ")
    print()