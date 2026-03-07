### **kwargs here (two asterick symbol is alone Want (kwargs is comment name or variable You can give any name))
###like *args its get as dictionaries,but the thing is It want positional Arguments with identifiers
def kwargsexample(**kwargs):
    for key,value in kwargs.items():
        print(value,end=" ")
kwargsexample(forhi="hi",firstname="sanjay",doing="You are doing great")

