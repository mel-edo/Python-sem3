# 2) write a python program to add three given lists using python map and lambda
arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 10]
arr3 = [11, 12, 13, 14, 15]

print(list(map(lambda x, y, z: x + y + z, arr1, arr2, arr3)))