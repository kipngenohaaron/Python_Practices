
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


num = '10'
 
# check and print type num variable
print(type(num))
 
# convert the num from string into int
converted_num = int(num)
 
# print type of converted_num
print(type(converted_num))
 
# We can check by doing some mathematical operations
print(converted_num + 20)

# Output
# <class 'str'>
# <class 'int'>
# 30
#convert an integer to a string
integer_number = 123
string_number = str(integer_number)
print(string_number)  # This will print "123"
