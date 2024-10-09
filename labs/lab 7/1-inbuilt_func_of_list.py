# 1) WAP to use various inbuilt functions of list

l1 = [1, 2, 3, 4, 5]
l1.append(5)
l2 = l1.copy()
print(l1.count(5))
print(l1.index(3))
l1.extend([100, 200])
l1.pop()
l1.remove(5)
l1.reverse()
l1.sort()
print(l1)
print(min(l1))
print(max(l1))

print(l2)
l2.clear()
print(l2)