# 1) Write a python program to triple all numbers in a list using python map

arr = [1, 2, 3, 4, 5]
def triple(x):
    return x * 3

# print(list(map(lambda x: x*3, arr)))
print(list(map(triple, arr)))

# l1 = list(map(int, input().split()))
# print(l1)