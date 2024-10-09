# 5) write a python program to square the elements of a list using the python map function
print(list(map(lambda x: x**2, list(map(int, input().split())))))