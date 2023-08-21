# if elif else
x = 10
if x % 3 == 0:
    print("x is divisible by 3")
elif x % 5 == 0:
    print("x is divisible by 5")
else:
    print("x is NOT divisible by 3 and 5")# Output: x is divisible by 5

# if elif
a=5
b=7
if a<b:
    print("a is less than b")

elif b < a :
 print("a is greater than or equal to b")# Output: a is less than b


# using break
a = 13
if a > 1:
    for x in range(2, a):
        if (a % x) == 0:
            print("NOT prime")
            break
    else:
        print("prime")# Output: prime

#Example of if else statement
x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")#Output: x is greater than 5

letter = "b"

if (letter == "a" or
    letter == "e" or
    letter == "i" or
    letter == "o" or
    letter == "u"):
    # Begin "if" block
    print("vowel.")
else:
    # Begin "else" block
    print("not a vowel.")

 #Example  
x = 0

while x < 10:
    print("so many loops")
    # output: infinite

name = "Steven"

print(f"Hi, {name}." if name != "Steven" else f"Goodbye, {name}.")#Goodbye, Steven.


name = "Steven"

print(f"Hi, {name}." if name == "Steven" else f"Goodbye, {name}.")# Hi, Steven.


def print_param(param):
    print(param)

string = print_param("hello")