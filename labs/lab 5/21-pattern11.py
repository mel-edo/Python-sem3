# 21) pattern:
'''
A
B A B
A B A B A
B A B A B A B'''
rows = 4
f = 0
for i in range(rows):
    for j in range(2 * i + 1):
        if f == 0:
            print("A", end=" ")
            f = 1
        else:
            print("B", end=" ")
            f = 0
    print()