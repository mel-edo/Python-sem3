# 5) WAP to compute the value of nCr
import math
n = int(input())
r = int(input())

# n!/r! * (n - r)!
print(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))