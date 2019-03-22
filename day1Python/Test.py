'''
Created on Mar 18, 2019

@author: rallamr
'''
from _ast import Num
from selenium.webdriver import opera

###        Removing spaces in between string        ###
a = "Lowes  India  PVT     LTD   "  
print(a.strip())
b=""
mylist = a.split(" ")
for lis in mylist:
    if(lis!=""):
        #print("It is not space")
        b = b+lis
print(b)


###        EVEN        ###

a = 101
for i in range(1,a):
    if(i%2==0):
        print(i)
        
        
        
###            REMOVE all occurances of 2            ###

li = [1,2,3,4,1,1,2,2,2,2,2]
li.remove(2)
print(li)


###            REVERSE the list            ###

li = [1,2,3,4,5,6,7,2]
li.reverse()
print(li)

li = [1,2,3,4,5,6,7,2]
li.sort(reverse=True)
print(li)



### Program to check number of char in a string
myStr = "Ramarao"
print(len(myStr))

### program to check given number is odd or even

a = 101
if(a%2==0):
    print("EVEN")
else:
    print("ODD")
### program to find sum in list num = [1,2,3,4,5] using for, while loops
sum = 0
numb = [1,2,3,4,5]
for i in numb:
    sum = sum+int(i)
print(sum)


sum = 0
numb = [6,7,8,9,10]
length = len(numb)
while(length!=0):
    length = length-1;
    sum = sum+numb[length]
print("Latest sum :",sum)




### Program to get elements from list fruits = ["apple","oranges","Grapes"]
fruits = ["apple","oranges","grapes"]
for i in fruits:
    print(i)
### program to demonstrate arthamatic operations by accepting user inputs

a = int(input("Enter the a value:"))
b = int(input("Enter the b value:"))
operator = input("Enter the operator:")
if(operator=="*"):
    print("Result: ",a*b)
elif(operator=="+"):
    print("Result: ",a+b)
elif(operator=="/"):
    print("Result: ",a/b)
elif(operator=="%"):
    print("Result: ",a%b)
else:
    print("Invalid operator")