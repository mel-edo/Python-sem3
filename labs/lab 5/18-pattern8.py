# 18) pattern:
'''
    *********
     *******
      *****
       ***
        *
'''
rows = 5
for i in range(rows):
    for j in range(i):
        print(" ", end="")
    for k in range(2 * (rows - i) - 1):
        print("*", end="")
    print()