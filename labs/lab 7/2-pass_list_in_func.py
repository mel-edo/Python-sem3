# 2) WAP to pass the list as an argument in the function
def square(list):
    res = []
    for i in list:
        res.append(i**2)
    return res

print(square([1, 2, 3, 4, 5]))