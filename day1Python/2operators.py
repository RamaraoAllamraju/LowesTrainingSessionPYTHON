'''
Created on Mar 18, 2019

@author: rallamr
'''
print(20/10)
print(20//10)

print(2**4)  ###2 power of 4

print("abc"=="abc")

if(5>10 or 10>1):
    print("1st IN IF BLOCK")


if(5>10 and 10>1):
    print("2nd IN IF BLOCK")
else:
    print("2nd ELSE BLOCK")
    
    
    
########    LOOPS AND CONDITIONS        ############


######         CONDITIONAL STATEMENTS            ######

## IF / ELSE

print("---------------------IF ELSE CHECK--------------------------------")

if(1==2):
    print("1==2")
else:
    print("1!=2")
    
if(1==2):
    print("in first block")
elif(5==2):
    print("in second block")
elif(5>1):
    print("in third block")


###########        LOOPS           #######
###            FOR LOOP            ###
###            WHILE               ###
print("--------------- LOOPS ---------------")
for i in range(1,11):
    print(i)
print("---")   
for i in "abc":
    print(i)
print("======================================")
a = 12
for i in range(1,a):
    print(i)
    
############################################

print("New")
a = 12
for i in range(1,a):
    print(i)
    if(i==5):
        break;
    
############################################

print("New123")
a = 12
for i in range(1,a):
    print(i)
    if(i!=5):
        continue;
    
###            WHILE            ###

print("WHILE")
i = 1
while i<=10:
    print(i)
    i=i+1
