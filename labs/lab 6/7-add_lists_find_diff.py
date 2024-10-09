# 7) write a python program to add 2 given lists and find differences between them using map

def add_lists(list1, list2):
    return list(map(lambda x, y: x + y, list1, list2))

def difference_lists(list1, list2):
    return list(map(lambda x, y: x - y, list1, list2))

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

if len(list1) != len(list2):
    print("Lists must be of the same length.")
else:
    sum_result = add_lists(list1, list2)
    difference_result = difference_lists(list1, list2)
    print(f"Sum of lists: {sum_result}")
    print(f"Difference of lists: {difference_result}")
