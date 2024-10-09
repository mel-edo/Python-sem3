# 9) wap to create a new list taking specific elements from a tuple and convert a string value to an integer

def list_tuple(input_tuple, indices):
    return [input_tuple[i] for i in indices]

tuple1 = (10, 20, 30, 40, 50)
indexes = [1, 3]

l1 = list_tuple(tuple1, indexes)

string_value = "123"
integer_value = int(string_value)

print(f"New list from the tuple: {l1}")
print(f"Converted integer value from string '{string_value}': {integer_value}")
