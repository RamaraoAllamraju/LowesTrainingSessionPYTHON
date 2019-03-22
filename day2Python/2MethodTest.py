'''
Created on Mar 19, 2019

@author: rallamr
'''
def Add(a,b):
    return a+b


def retTest():
    return 10,"ram"

#####################################################

print(Add(10,20))

# We can return multiple values from a function.
val,name = retTest()
print("Val :"+str(val)+" Name :"+name)

val = retTest()
print(val)

#####################################################