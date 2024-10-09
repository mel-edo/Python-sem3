# 6) WAP to generate the fibonacci series
# 0, 1, 1, 2, 3, 5, 8
cache = [0, 1]
n = int(input())
cur = 1
for i in range(n - 2):
    cache.append(cache[cur] + cache[cur - 1])
    cur += 1
    n += 1
print(cache)