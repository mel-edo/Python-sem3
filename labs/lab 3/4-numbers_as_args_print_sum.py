# 4) To take numbers as command line arguments and print its sum
input_string = input("Enter numbers separated by spaces: ")

args = input_string.split()

numbers = [int(arg) for arg in args]

total = sum(numbers)

print("The sum is: ", total)