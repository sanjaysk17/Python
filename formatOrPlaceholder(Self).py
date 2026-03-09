##placeholder is done by the function format(),for eg given below
animal="lion"
print("The {} is king in jungle".format(animal))#Normal
print("The {flower} is beautiful".format(flower="Rose"))##Keyword Argument
name="sanjay"
print("The statement is written by {0} and He like {1}".format(name,animal))

##For padding you give like {:10} or  {:<10} or {:>10} orv{:=10}

print("The {:10} is king in jungle".format(animal))#for Right
print("The {:>10} is king in jungle".format(animal))#for Left
print("The {:^10} is king in jungle".format(animal))#FOr center

#For only 2 point or any other Point After Decimal.. and Number COnversation

num=10
print("The {:.2f} is a number".format(num))
print("The {:b} is a number".format(num))
print("The {:o} is a number".format(num))
print("The {:X} is a number".format(num))
#Output
"""sanja@Sanjay MINGW64 /d/Python (main)
$ python formatOrPlaceholder\(Self\).py 
The lion is king in jungle
The Rose is beautiful
The statement is written by sanjay and He like lion
The lion       is king in jungle
The       lion is king in jungle
The    lion    is king in jungle
The 10.00 is a number
The 1010 is a number
The 12 is a number
The A is a number"""