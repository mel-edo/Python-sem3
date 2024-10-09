# 4) write a python program to create a list containing the power of said number in bases raised to the coreresponding number in the index using map
def generate_powers(base, length):
    return list(map(lambda x: base ** x, range(length)))

base_number = int(input("Enter the base number: "))
list_length = int(input("Enter the length of the list: "))

result = generate_powers(base_number, list_length)
print(f"Powers of {base_number} from 0 to {list_length - 1}: {result}")