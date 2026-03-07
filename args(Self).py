##Args get as a tuple as like a list but immutable Without * it fails (any Variable can beside the this symbol *)
def add(*args):
    sum=0
    for i in args:
        sum=sum+i
    print(sum)
add(1,2,3,4,5)
#Without *
"""def add(num1,num2):
    sum=num1+num2
    print(sum)
add(1,2,3,4,5)

"""
##This give me only error
"""$ python args.py 
Traceback (most recent call last):
  File "D:\Python/args.py", line 8, in <module>
    add(1,2,3,4,5)
    ~~~^^^^^^^^^^^
TypeError: add() takes 2 positional arguments but 5 were given"""
