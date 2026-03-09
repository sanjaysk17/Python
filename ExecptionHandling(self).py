#Exception means events detected during Execution that interrupt the flow of a Program

try:
    num1=int(input("Enter a Number:"))
    num2=int(input("Enter a Number2"))
    result=num1/num2
except ZeroDivisionError as e:#as e for Its Print error like this "division by zero"
    print(e)
    print("The denominator is Zero")
except ValueError:
    print("The input Value may be any Other than Int")
else:
    print(result)



#output:
"""
$ python ExecptionHandling\(self\).py 
Enter a Number:9
Enter a Number20
division by zero
The denominator is Zero

"""