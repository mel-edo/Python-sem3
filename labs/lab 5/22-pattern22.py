# 22) pattern:
'''
1
0 1 0
1 0 1 0 1
0 1 0 1 0 1 0'''
rows = 4
f = 0
for i in range(rows):
    for j in range(2 * i + 1):
        if f == 0:
            print(1, end=" ")
            f = 1
        else:
            print(0, end=" ")
            f = 0
    print()