'''
Created on Mar 19, 2019

@author: rallamr
'''

## 4

class operone():
    x = 100
    y = 20
    
    def add(self):
        return self.x+self.y
    
    def sub(self):
        return operone.x-operone.y 

# Inheritance - by just passing the parent class as parameter
class opertwo(operone):
    def mult(self):
        return operone.x*operone.y
    
two = opertwo()
print(two.sub())

print(operone.add(operone))

