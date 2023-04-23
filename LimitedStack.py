'''
Hey there! This is Lab 7b for CSCI 161 Summer 2021
Creates a class object that behaves as a stack
datastructure. Similar to ListStack but updated
push method. This version of push removes last item
in stack and shifts all items down to accomodate new item.
By Kevin Jordan kevin.jordan@und.edu 1301006 (and Tom Stokke UND)
'''

class LimitedStackError (Exception):
    pass

class LimitedStack:

    def __init__ (self, maxSize=10):
        self.__stack = [None] * maxSize
        self.__maxSize = maxSize
        self.__numOfItems = 0

    def push (self, itemToPush):
        if not self.isFull():
            self.__stack[self.__numOfItems] = itemToPush
            self.__numOfItems += 1
        else:
            for i in range(0, (self.__numOfItems-1)):
                self.__stack[i] = self.__stack[i+1]
            self.__stack[self.__numOfItems -1] = itemToPush
                         
    def pop (self):
        if not self.isEmpty():
            itemToReturn = self.__stack[self.__numOfItems - 1]
            self.__stack[self.__numOfItems - 1] = None #NOT required, as this location will be overwritten next push and will not be accessed by peek
            self.__numOfItems -= 1
            return itemToReturn
        #  or 
        #  self.__numOfItems -= 1
        #  return self.__stack[self.__numOfItems]
        else:
            raise ListStackError ("Unable to peek from an empty stack")


    def peek (self):
        '''
        peek returns the top (most recently added) item from the stack

        Raises a ListStackError if called upon an empty stack
        '''
        if not self.isEmpty():
            return self.__stack[self.__numOfItems - 1]
        else:
            raise ListStackError ("Unable to peek from an empty stack")


    def top (self):
        '''
        top removes the top (most recently added) item from the stack

        Raises a ListStackError if called upon an empty stack
        '''
        if not self.isEmpty():
            self.__stack[self.__numOfItems - 1] = None #NOT required, as this location will be overwritten next push and will not be accessed by peek
            self.__numOfItems -= 1
        else:
            raise ListStackError ("Unable to peek from an empty stack")

    def isEmpty (self):
        return self.__numOfItems == 0

    def isFull (self):
        return self.__numOfItems == self.__maxSize

    def maxSize(self):
        return self.__maxSize

    def __str__ (self):
        #if I was doing this "for real" I might do this:
        #return "ListStack object - version 0.91, last updated 7/15/2021."
        strData = "Data: "
        for index in range (0, self.__numOfItems):
            strData += self.__stack[index] +  '  '
        return strData   