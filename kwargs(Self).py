"""
Example of **kwargs in Python

**kwargs allows a function to accept a variable number of
keyword arguments. The arguments are stored as a dictionary.

Note:
- '**' is the important part.
- 'kwargs' is just a variable name. You can use any name.
"""

def kwargsexample(**kwargs):
    # kwargs becomes a dictionary
    for key, value in kwargs.items():
        print(value, end=" ")

# Calling the function with keyword arguments
kwargsexample(forhi="hi", firstname="sanjay", doing="You are doing great")