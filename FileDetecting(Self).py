#File Detecting
import os

path ="C:\\Users\\sanja\\Desktop\\Hello.txt"##Path is Existed in my Laptop you want to run means Change the file path According to you"

if os.path.exists(path):
    print("Path Exist")
    if os.path.isfile(path):
        print("It is a File")
elif os.path.isdir(path):
    print("Its is directory")