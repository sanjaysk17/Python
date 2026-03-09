text='Hi iam Written with\n Python in thif file \n thank you'
##For Writing
with open("ForReadingANDWriting.txt",'w') as file:
    file.write(text)
##For Appending
forAppend="text Appended"
with open("ForReadingANDWriting.txt",'+a') as file:
    file.write(forAppend)
##For Reading
with open("ForReadingANDWriting.txt",'r') as file:
    print(file.read())