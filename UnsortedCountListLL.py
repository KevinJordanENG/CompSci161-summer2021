'''
Hey there! This is Lab 9 for CSCI 161 Summer 2021
Creates a class object that creates a fixed length linked list.
Includes numerous methods such as add, remove, size, 
overallCount, count, isInList, isFull, isEmpty, reset, getNextItem.
Uses the inner class structure to keep count of same values.
By Kevin Jordan kevin.jordan@und.edu 1301006 (and Tom Stokke UND)
'''

class UnsortedCountListLL:
    
    class __Node:                  
        def __init__(self, data):
            self.data = data
            self.count = 1
            self.next = None

    def __init__ (self, maxSize=100):
        self.__maxSize = maxSize
        self.__numOfItems = 0
        self.__head = None
        self.__tail = None
        self.__currentNode = None
        self.__iterNode = None
            
    def isFull(self):            
        return self.__numOfItems == self.__maxSize    
    
    def isEmpty(self):      
        return self.__numOfItems == 0     

    def isInList (self, itemToFind):
        location = self.__head
        while location != None:
            if location.data == itemToFind:    
                return True
            location = location.next
        return False        
    
    def size(self):          
        return self.__numOfItems
    
    def reset(self):       
        self.__currentNode = self.__head
        
    def getNextItem(self):   
        if self.isEmpty():
            raise Exception("Sorry, list is empty")
        if self.__currentNode == None:
            self.__currentNode = self.__head        
        itemToReturn = self.__currentNode.data  
        self.__currentNode = self.__currentNode.next
        if self.__currentNode == None:
            self.__currentNode = self.__head        
        return itemToReturn          
    
    def add(self, itemToAdd):
        if not self.isFull():                    
            if not self.isInList(itemToAdd):    
                newNode = UnsortedCountListLL.__Node(itemToAdd)
                newNode.next = self.__head
                self.__head = newNode 
                if self.__tail == None:
                    self.__tail = newNode      
                self.__numOfItems += 1                                                  
                return True
            else:
                location = self.__head
                while location != None:
                    if location.data == itemToAdd:
                        location.count += 1
                        return True
                    location = location.next                
        return False
    
    def count(self, item):
        if self.isInList(item):
            location = self.__head
            while location != None:
                if location.data == item:    
                    return location.count
                location = location.next              
        else:
            return 0
    
    def overallCount(self):
        total = 0
        location = self.__head
        while location != None:
            total += location.count
            location = location.next           
        return total
    
    def remove(self, itemToRemove):
        if not self.isEmpty():                   
            if self.isInList(itemToRemove):          
                location = self.__head
                while location != None:
                    if location.data == itemToRemove:
                        if location.count > 1:
                            location.count -= 1
                            return True
                        else:
                            if self.__head.data == itemToRemove:
                                self.__head = self.__head.next
                                if self.__tail.data == itemToRemove:
                                    self.__tail = None 
                                self.__numOfItems -= 1   
                                return True  
                            else:
                                prevNode = self.__head  
                                location = self.__head.next 
                                while location != None: 
                                    if location.data == itemToRemove:
                                        if location.next == None: 
                                            self.__tail = prevNode
                                        prevNode.next = location.next    
                                        self.__numOfItems -= 1
                                        return True
                                    else:
                                        prevNode = location
                                        location = location.next                            
                    location = location.next    
        return False