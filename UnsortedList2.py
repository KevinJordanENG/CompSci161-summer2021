'''
Hey there! This is Lab 4 for CSCI 161 Summer 2021
Creates a class object that creates a fixed length list.
Includes numerous methods such as add, remove, isInList,
isFull, isEmpty, getNextItem, size, reset, findIndexOf,
removeAll, replaceAll, count, partialMatch
By Kevin Jordan kevin.jordan@und.edu 1301006 (and Tom Stokke UND)
'''

class UnsortedList2MatchException (Exception):
   pass

class UnsortedListAddError (Exception):
   pass #must have at least one line of code in a code, but I don't really want to add anything

class UnsortedListGetNextItemError (Exception):
   pass #must have at least one line of code in a code, but I don't really want to add anything
   
class UnsortedList2:
   
   def __init__ (self, maxSize=10):
      self.__data = [None] * maxSize #create the entire list, with each item having the value None
      self.__numOfItems = 0
      self.__maxSize = maxSize #will be the same as len(self.__data)
      self.__currentItem = 0 #index of item to be returned by getNextItem
      self.__nextLocation = 0 #index of item to be returned by __next__ (working with for loop)
      
   
      '''
      add method accepts a single item to add to the unsorted list. 
      No checking is performed to test is itemToAdd is currently in the list.
      
      add raises an Exception error if unable to add itemToAdd to the list, otherwise nothing is returned
      '''
   def add (self, itemToAdd):
      if not self.isFull(): # or if self.isFull() == False:
         self.__data[self.__numOfItems] = itemToAdd
         self.__numOfItems = self.__numOfItems + 1
      else:
         #raise leaves the function NOW, with info about the exception stored in the returned Exception object
         #raise Exception ("ULError - Unable to add " + itemToAdd + " to a full UnsortedList") #Exception is a generic exception
         raise UnsortedListAddError ("ULError - Unable to add " + itemToAdd + " to a full UnsortedList")

   def isFull(self):   
      return self.__numOfItems == self.__maxSize
      #if self.__numOfItems == self.__maxSize:
      #   return True
      #else:
      #   return False
   
   def isEmpty(self):
      return self.__numOfItems == 0
   
   '''
   improved remove
   found the item to remove, then replaced it with the last item
   Big O - n, but a "better" n than remove2 :-)
   '''
   def remove (self, itemToRemove):
      for index in range ( 0, self.__numOfItems):
         if self.__data[index] == itemToRemove:
            self.__data[index] = self.__data[self.__numOfItems - 1]
            self.__data[self.__numOfItems-1] = None
            self.__numOfItems -= 1
            return True   

      return False         

   '''
   private function (function name starts with double underscore "__") to return the index of itemToFind
   returns -1 is itemToFind does not exist in the list
   '''
   
   def __findIndexOf (self, itemToFind):
      for index in range ( 0, self.__numOfItems):
         if self.__data[index] == itemToFind:
            return index 
      return -1 #loop is done and we didn't return an index from the previous line, so that tells us it's not in the list   

   def isInList (self, itemToFind):
      return self.__findIndexOf (itemToFind) >= 0
   
   def size(self):
      return self.__numOfItems
   
   def reset(self):
      self.__currentItem = 0
      
   def getNextItem(self):
      valueToBeReturned = self.__data[self.__currentItem]
      self.__currentItem += 1
      #if we want to wrap around once we get to the end
      if self.__currentItem == self.__numOfItems: #compare current item to num of items, NOT max size
         self.__currentItem = 0 #if we want to wrap around once we get to the end of our data
      #if we want to raise an exception if we get to the end 
      #if self.__currentItem > self.__numOfItems: #compare current item to num of items, NOT max size
      #   raise Exception ("UnsortedList getNextItem error - accessing beyond data limits") #if we want to raise an exception if we go past the end of the data
      return valueToBeReturned
   
   def __iter__ (self):
      return self
      
   def __next__ (self):
         if self.__nextLocation == self.__numOfItems: #we're past the end of the data 
            self.__nextLocation = 0 #set ourself up for the next time the for loop is used to access the data
            raise StopIteration
            
         temp = self.__data[self.__nextLocation]
         self.__nextLocation += 1
         return temp
      
   def removeAll(self, itemToRemove):
      numMatching = 0
      for index in range ( 0, self.__numOfItems):
         if self.__data[index] == itemToRemove:
            numMatching += 1
            self.__data[index] = self.__data[self.__numOfItems - 1]
            self.__data[self.__numOfItems-1] = None
            self.__numOfItems -= 1
      for index in range ( 0, self.__numOfItems):
         if self.__data[index] == itemToRemove:
            numMatching += 1
            self.__data[index] = self.__data[self.__numOfItems - 1]
            self.__data[self.__numOfItems-1] = None
            self.__numOfItems -= 1      
      return numMatching
   
   def replaceAll(self, newValue, originalValue):
      numMatching = 0
      for index in range ( 0, self.__numOfItems):
         if self.__data[index] == originalValue:      
            self.__data[index] = newValue
            numMatching += 1
      return numMatching
   
   def count(self, valueToCount):
      numMatching = 0
      for index in range ( 0, self.__numOfItems):
         if self.__data[index] == valueToCount:      
            numMatching += 1
      return numMatching
   
   def partialMatch(self, itemToFind=None):
      if itemToFind == None:
         raise UnsortedList2MatchException("No item to find specified")
      matches = []
      for index in range ( 0, self.__numOfItems): 
         if self.__data[index].find(itemToFind) != -1:
            matches.append(self.__data[index])
      return matches