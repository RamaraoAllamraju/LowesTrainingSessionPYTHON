'''
Created on Mar 19, 2019

@author: rallamr
'''
###5

###            OVERRIDING            ###
#Method overriding will only be possible if there is INHERITANCE

print("###OVERIDING###")
class test():
    def printMsg(self):
        print("First test class")

class newtest(test):
    def printMsg(self):
        print("In second class")
    
obj = newtest()
obj.printMsg()

###            OVER LOADING            ###
print("###OVERLOADING###")
class loadtest():
    def printMess(self):
        print("Hello")
class newloadtest():
    def printMess(self,myStr):
        print(myStr)

newobj = newloadtest()
newobj.printMess("I am good")

#newobj.printMess()


###            CONSTRUCTORS            ###

print("###CONSTRUCTOR###")

class constTest():
    def __init__(self):
        print("In normal constructor")
    def test(self,myMsg):
        print(myMsg)
obj = constTest()
obj.test("HI")


print("###CONSTRUCTOR TWO###")
class constTestTwo():
    def __init__(self, mynewMsg):
        print("In normal constructor  "+mynewMsg)
    def test(self,myMsg):
        print(myMsg)
obj = constTestTwo("I am sending message")
obj.test("HI")

