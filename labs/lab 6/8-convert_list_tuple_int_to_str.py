# 8) wap to convert a given list of integers and a tuple of integers in a list of strings

def convert_to_strings(input_collection):
    return list(map(str, input_collection))

integer_list = [1, 2, 3, 4, 5]
integer_tuple = (6, 7, 8, 9, 10)

list_of_strings = convert_to_strings(integer_list)
tuple_of_strings = convert_to_strings(integer_tuple)

print(f"List of strings from the list: {list_of_strings}")
print(f"List of strings from the tuple: {tuple_of_strings}")
