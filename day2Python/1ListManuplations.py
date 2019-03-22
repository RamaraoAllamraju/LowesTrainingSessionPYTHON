'''
Created on Mar 19, 2019

@author: rallamr
'''


li = [5,125,1,25,63]
li.reverse()
print(li)

li2 = li    #li1 = li.copy()

print(li2)

li3 = [100,1201,123]

li.extend(li3)
print(li)