# 6) write a python program to convert all characters into uppercase and lowercase and eliminate duplicate letters from given sequence using map
seq = input()

uppercase = "".join(list(map(lambda x: x.upper(), seq)))
lowercase = "".join(list(map(lambda x: x.lower(), seq)))

duplicates_upper = "".join(dict.fromkeys(uppercase))
duplicates_lower = "".join(dict.fromkeys(lowercase))

print(uppercase)
print(lowercase)
print(duplicates_upper)
print(duplicates_lower)