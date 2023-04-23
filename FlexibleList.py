'''
Hey there! This is Lab 3b for CSCI 161 Summer 2021
Creates a class object that creates a fixed length list
and can have custom indexes set.
By Kevin Jordan kevin.jordan@und.edu 1301006
'''

class FlexibleList:
    
    def __init__(self, lowIndex, highIndex, defaultValue = None):
        
        self.__data = [defaultValue] * (highIndex-lowIndex)
        self.__lowIndex = lowIndex
        self.__highIndex = highIndex
        
    def get(self, index):
        if (index < self.__lowIndex) or (index > self.__highIndex):
            raise Exception("OutOfRangeError - Out of range of FlexibleList")
        else:
            return self.__data[index-self.__lowIndex]
    
    def set(self, index, value):
        if (index < self.__lowIndex) or (index > self.__highIndex):
            raise Exception("OutOfRangeError - Out of range of FlexibleList")        
        else:
            self.__data[index-self.__lowIndex] = value
        
    def lowIndex(self):
        return self.__lowIndex
    
    def highIndex(self):
        return self.__highIndex
    
    def isInList(self, itemToFind):
        for index in range(self.__highIndex - self.__lowIndex):
            if self.__data[index] == itemToFind:
                return True
        return False
    
    def indexOf(self, itemToFind):
        for index in range(self.__highIndex - self.__lowIndex):
            if self.__data[index] == itemToFind:
                return index + self.__lowIndex
        return None