'''
Created on Mar 18, 2019

@author: rallamr
'''




from audioop import reverse
myLi = []
print(myLi)


myLi = [1,2,3,4]
print(myLi)

myLi = list((5,6,7,8,9))
print(myLi)

myLi=["Ram","Rao","Allamraju","Ramarao","Ram"]
for i in myLi:
    print(i)

print("Now using another way of printing")
for i in range(0,len(myLi)):
    print(myLi[i])
    
print("Now using an another way of printing without lower limit in range")
for i in range(len(myLi)):
    print(myLi[i])
    
print(myLi.count("Ram"))
    
    
myLi = []
myLi.append("Ram")
print(myLi)
myLi.append("Rao")
print(myLi)
myLi.append("Allam")
print(myLi)

myLi2 = ["9908448819",8970370683]
print(myLi2)
myLi2.append(897037)
print(myLi2)
######
myLi.append(myLi2)
print(myLi)
######

myLi2.insert(1, "HAHAHA")
print(myLi2)

#for i in range(0,10):
#    print(myLi[i])
myLi=[1,2,3,4]
print(myLi)
myLi[2]="HAHA"
print(myLi)

myLi.remove("HAHA")   ## REMOVES based on value
print(myLi)

myLi.pop(2)     ## POP removes based in INDEX
print(myLi)

###            SORTING            ###
myLi = [12,52,11,10,4,78,99,3,2,12,52]
print(myLi)
myLi.sort()
print(myLi)
myLi.sort(reverse=True)
print(myLi)

myStrList = ["Rama","Allam","Anthony"]
print(myStrList)
myStrList.sort()
print(myStrList)
myStrList.sort(reverse=True)
print(myStrList)

myLi.sort(reverse=False)
myLi.sort(reverse=False)
print(myLi)




myDic = [(10,2,115,20),(21,58,56,1),(5,25,65,2),(15,25,65,12)]
#print(myDic)
#myDic.sort()
#print(myDic)

def myMet(ele):
    return ele[2]

myDic.sort(key=myMet,reverse=True)
print(myDic)

