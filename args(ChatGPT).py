"""
Demonstration of *args in Python

*args allows a function to accept a variable number of
positional arguments. The values are stored as a tuple
(which is similar to a list but immutable).
"""

def add(*args):
    total = 0
    for i in args:
        total = total + i
    print("Sum:", total)


# Run the function
add(1, 2, 3, 4, 5)


"""
Example WITHOUT *args

def add(num1, num2):
    total = num1 + num2
    print(total)

add(1,2,3,4,5)

Error produced:

TypeError: add() takes 2 positional arguments but 5 were given
"""

