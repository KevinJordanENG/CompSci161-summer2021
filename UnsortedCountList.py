'''
Hey there! This is Lab 6 for CSCI 161 Summer 2021
Creates a class object that creates a fixed length list.
Includes numerous methods such as add, remove, size, 
overallCount, count, isInList, isFull, isEmpty, reset, getNextItem.
Uses the inner class structure to keep count of same values.
By Kevin Jordan kevin.jordan@und.edu 1301006 (and Tom Stokke UND)
'''

class UnsortedCountList:                    #main class
    class __Strings:                        #inner class
        def __init__(self, string):
            self.string = string            #initialize string and its counter
            self.count = 1   

    def __init__ (self, maxSize=100):
        self.__data = [None] * maxSize #create the entire list, with each item having the value None
        self.__numOfItems = 0
        self.__maxSize = maxSize #will be the same as len(self.__data)
        self.__currentItem = 0 #index of item to be returned by getNextItem
        self.__nextLocation = 0 #index of item to be returned by __next__ (working with for loop)
            
    def isFull(self):               #returns bool for if list is maxed out
        return self.__numOfItems == self.__maxSize    
    
    def isEmpty(self):              #returns bool for if list is empty
        return self.__numOfItems == 0     

    def isInList (self, itemToFind):
        for i in range(0, self.__numOfItems):
            if self.__data[i].string == itemToFind:   #if the inner class instance var of string matches
                return True
        return False
    
    def size(self):             #how many unique objects
        return self.__numOfItems
    
    def reset(self):            #resets current item to 0
        self.__currentItem = 0
        
    def getNextItem(self):      #gets current item iterates current position counter
        valueToBeReturned = self.__data[self.__currentItem].string
        self.__currentItem += 1
        if self.__currentItem == self.__numOfItems:
            self.__currentItem = 0      #loops around if at the end and starts at beginning
        return valueToBeReturned    
    
    def add(self, itemToAdd):
        if not self.isFull():                       #if not full
            if not self.isInList(itemToAdd):        #if entry is new unique string
                self.__data[self.__numOfItems] = UnsortedCountList.__Strings(itemToAdd) #create an inner class object
                self.__numOfItems += 1                                                  #with the same name as string
                return True
            else:
                for i in range(0, self.__numOfItems):   #if its not unique and already is in list
                    if self.__data[i].string == itemToAdd:  #find its position
                        self.__data[i].count += 1           #increment counter
                        return True
        return False
    
    def count(self, item):
        if self.isInList(item):                     #if in the list
            for i in range(0, self.__numOfItems):   #find it
                if self.__data[i].string == item:
                    return self.__data[i].count     #return how many it has
        else:
            return 0
    
    def overallCount(self):
        total = 0
        for i in range(0, self.__numOfItems):           #for all items in list
            total = total + self.__data[i].count        #total their counts
        return total
    
    def remove(self, itemToRemove):
        if not self.isEmpty():                          #if not empty
            if self.isInList(itemToRemove):             #and its in the list
                for i in range(0, self.__numOfItems):
                    if self.__data[i].count > 1:        #if more it has more than 1 count
                        self.__data[i].count -= 1       #decrement count but dont competely delete
                        return True
                    else:                   #if its only or last count, remove it completely
                        self.__data[i] = self.__data[self.__numOfItems - 1]
                        self.__data[self.__numOfItems-1] = None
                        self.__numOfItems -= 1      #reduce number of items in list
                        return True
        return False