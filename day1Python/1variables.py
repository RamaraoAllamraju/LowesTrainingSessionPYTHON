'''
Created on Mar 18, 2019

@author: rallamr
'''
from numpy.core.defchararray import upper
a,b=10,20
print(a,b)
print(type(a))
#The above results in <class 'int'> --> in python everything is an object
# so, a is of type int

#################################################################################

###Data types###
###int###
###float###
###string###
###boolean###

print(type(10))
print(type(10.2))
print(type("Ram"))
print(type(True)) #T should be caps & For false it is False

###################################################################################

#input function takes input from user and it takes as a string

a = input("Enter :")
print(a)
print("A type is :",type(a))
#type casting 
# we can do for int str float

a = int(input("Enter :"))
print(a)
print("A type is :",type(a))
print(a+10)

a = float(input("Enter :"))
print(a)
print("A type is :",type(a))
print(a+10)


#######################################################################################

#String

a = 'Lowe\'s'
print(a)

inputString = input("Enter user name:")
print(len(inputString))

##Verify duplicates
a="Ramarao"
print(a.count("a"))
print("----------------------")
a="Day 1 learning include variables and methods for day1 training"
print(a.count("day"))
print(a.count("Day"))

print(a.find("learning"))

print(a.find("l"))
print(a.find("z"))

print(a.index("l"))     
### If the string not found then index will throw an exception, but find will not
#print(a.index("z"))

##StartsWith

a = "EMP123"
print(a.startswith("EMP"))
print(a.startswith("INEMP"))
print(a.endswith("EMP"))

a = "123EMP"
print(a.endswith("EMP"))

###UPPER AND LOWER
print(a.upper())
print(a.lower())

b = "ramarao"
print(upper(b))

##SPLIT

a = "Python36-32-43"

print(a.split("-"))
print(a.split("-",1))

myList = a.split("-")
print(myList)

##JOIN
b = "++"
print(b.join(myList))

##STRIP removing spaces at start and end but not in between the characters

a = " Ram is     working in        lowes         "
print(a.strip())
b=" "
newlist = a.split(" ")
for a in newlist:
    if(a==" "):
        print("In if")
        b=b+a
print("Printing b")
print(b)


#Replace
a = "Ram works in lowes"
print(a.replace("Ram", "Ramarao"))

#Multiple
a = "Ram"
a = a*3
print(a)