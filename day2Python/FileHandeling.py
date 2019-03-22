'''
Created on Mar 19, 2019

@author: rallamr
'''
from openpyxl.compat.strings import file
from lib2to3.tests.data.infinite_recursion import FILE
path = "C:/Users/rallamr/Desktop/Ramarao/Eclipse Workspace/LowesTrainingSessionPYTHON/files/test.txt"
path1 = "C:/Users/rallamr/Desktop/Ramarao/Eclipse Workspace/LowesTrainingSessionPYTHON/files/test1.txt"

class FileActions():
    def readFile(self):
        fileObj = open(path,"r")
        print(fileObj.read())
        fileObj.close
    def writeFile(self):
        fileObj = open(path,"w")
        fileObj.write("I am writing")
        fileObj.close
    def appendFile(self):
        fileObj = open(path, "a")
        fileObj.write("I am appending this to the file")
        fileObj.close
    def createFile(self):
        fileObj = open(path1,"x")
        fileObj.write("This is new text in new file")
        fileObj.close
    def readLineByLine(self):
        fileObj = open(path,"r")
        line = fileObj.readline()
        for i in line:
            print(i)
            print("One line printed")
fa = FileActions()
'''fa.readFile()
fa.writeFile()
fa.readFile()
fa.appendFile()
fa.readFile()
fa.createFile()'''

fa.readLineByLine()
