'''
Created on Mar 19, 2019

@author: rallamr
'''
class oper():
    a = 100
    b = 200
    def add(self):
        #a = 10
        #b = 20
        return oper().a+oper().b
    
    
#print(oper.add(oper()))

class operanoth():
    a = 100
    b = 200
    def sub(self):
        #a = 10
        #b = 20
        return oper().a-oper().b
    
    
    
### OVER LOADING IN SAME CLASS
class test():
    def myMeth(self):
        print("Test")
#    def myMeth(self,myStr):
#        print(myStr)
        
obj = test()
obj.myMeth("Hello")