# avg of 2 numbers and print their deviation
a = int(input("1st: "))
b = int(input("2nd: "))
res = (a + b) / 2
deviation_a = a - res
deviation_b = b - res
print(res)
print(deviation_a, deviation_b)