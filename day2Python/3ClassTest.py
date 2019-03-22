'''
Created on Mar 19, 2019

@author: rallamr
'''
class Operators():
    a = 10
   
    #Self will be having the address of the particular object
    # add and getValue are non-static methods
    #self parameter will be there for non-static methods
    def add(self):
        a,b = Operators().getValue()
        return a+b
    def getValue(self):
        return 100,200
    
    #The below is the static method, for that we need to use decorators
    
    
    @staticmethod
    def sub():
        #The below commented code and the other both works
        #a,b = Operators.getValue(Operators)
        a,b = Operators().getValue()
        return b-a
    
print(Operators().a)

op = Operators()
print(op.add())
#Below is one way of calling a non-static methods
print(Operators.add(op))

print(op.sub())
print(Operators.sub())