'''
Created on Mar 19, 2019

@author: rallamr
'''
try:
    print(10/0)
except Exception as msg:
    print(msg)
    
## TRY ELSE
## IF no exception then it will go to else block

try:
    print(10/2)
except Exception as msg:
    print(msg)
else:
    print("I am here")

## FINALLY

try:
    print(10/0)
except Exception as msg:
    print(msg)
else:
    print("I am Second here")
finally:
    print("In finally")


try:
    print(10/10)
except Exception as msg:
    print(msg)
else:
    print("I am third here")
finally:
    print("Finally in Final")
