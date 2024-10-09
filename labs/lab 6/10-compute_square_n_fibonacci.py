# 10) wap to compute the square of first n fibonacci numbers using map and generate a list of numbers
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def square(x):
    return x * x

def square_of_fibonacci(n):
    fib_numbers = fibonacci(n)
    squared_fib_numbers = list(map(square, fib_numbers))
    return squared_fib_numbers

n = 10
print(square_of_fibonacci(n))