# 2) User inputted list of 25 elements, find mean, median and mode
from collections import Counter
import random
l1 = []
for i in range(2000):
    l1.append(random.randint(1, 100))
print("mean: ", sum(l1) / len(l1))

orig_l1 = l1.copy()

l1.sort()
median = l1[len(l1) // 2]
print("median: ", median)

d1 = dict(Counter(l1))
freq = 1
mode = 1
for i in d1:
    if d1[i] > freq:
        mode = i
        freq = d1[i]
print("mode: ", mode)

# slice that list into 5 lists, merge even lists and odd lists together i.e 1st, 3rd and 5th merge together and 2nd and 4th merge together

arr_sublists = []
p1 = 0
p2 = 5
while p2 <= len(orig_l1):
    arr_sublists.append(orig_l1[p1:p2])
    p1 += 5
    p2 += 5

odd_arr = []
even_arr = []
# merging even number arrays
for i, v in enumerate(arr_sublists):
    if i % 2 == 0:
        even_arr.extend(v)
    else:
        odd_arr.extend(v)

print("Even arr: ", even_arr)
print("Odd arr: ", odd_arr)

