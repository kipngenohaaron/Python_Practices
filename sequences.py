
def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < length:
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
        print(fib_sequence)

# Test cases
print_fibonacci(0)   # Output: []
print_fibonacci(1)   # Output: [0]
print_fibonacci(2)   # Output: [0, 1]
print_fibonacci(10)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#convert a string to an integer
string_number = "123"
integer_number = int(string_number)
print(integer_number)  # This will print 123
