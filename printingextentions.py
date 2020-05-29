
#program to accept a filename from the user and print the extention of that

filename = input("Input the Filename: ")# here the user will input a filename
f_extns = filename.split(".")# this function is used for printing extension of a file in python
print ("The extension of the file is : " + repr(f_extns[-1])) # the extention of the filename entered by the user is printed
