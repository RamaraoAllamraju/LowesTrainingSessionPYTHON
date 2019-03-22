'''
Created on Mar 18, 2019

@author: rallamr
'''
###LIST
###TUPLE
###SET
###DICTONARY

############################     LIST     #########################################

# We will represent a list enclosed in a SQUARE BRACKETS []
# It will allow duplicate values
a = ["LOWES","INDIA",12,"@$",12.3,52]
print(a)
print(type(a))


##############################     TUPLE      #####################################

# We will represent a TUPLE enclosed in a round brackets ()
# We can't add data once it is defined
# It allows duplicates

a = ("Lowes","INDIA",12,12.36)
print(a)
print(type(a))

##############################     SET      #####################################

# We will represent a SET enclosed in a curly brackets {}
# Will not allow duplicate values

a = {"Lowes","INDIA",12,23.6}
print(a)
print(type(a))

b = {"Lowes","INDIA","Lowes","LOWES"}
print(b)

##############################     DICTONARY      #####################################

# It is a key value pair
# Key cannot be duplicate
# We can represent in curly brackets {"key":"value","key1":"value"}

a = {"company":"Lowes","Location":"Banglore"}
print(a)
print(type(a))

print(a["Location"])