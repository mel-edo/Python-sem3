# 17) pattern:
'''
        1
      2 3 2
    3 4 5 4 3
  4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5'''
rows = 5
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for j in range(i, 2 * i):
        print(j, end=" ")
    for j in range(2 * i - 2, i - 1, -1):
        print(j, end=" ")
    print()