'''
Hey there! This is Lab 11a for CSCI 161 Summer 2021
Creates a class object that uses linked lists to
generate a sparse array. Supports methods of get,
getDefaultValue, and set.
By Kevin Jordan kevin.jordan@und.edu 1301006
'''

class SparseArrayException(Exception):
    pass

class SparseArray:
    
    class __Node:           
        def __init__(self, index, data):
            self.data = data            #data to be put in array
            self.index = index          #'index' of array node
            self.next = None
    
    def __init__(self, defaultValue, maxSize = 10000):
        self.__maxSize = maxSize            #initialize instance variables
        self.__defaultValue = defaultValue
        self.__numOfItems = 0
        self.__head = None
        self.__tail = None
        for i in range(maxSize):            #initialize maxSize number of nodes to defaultValue
            newNode = SparseArray.__Node(i, defaultValue)
            newNode.next = self.__head
            self.__head = newNode 
            if self.__tail == None:
                self.__tail = newNode      
            self.__numOfItems += 1
            
    def getDefaultValue(self):          #returns defaultValue
        return self.__defaultValue
    
    def get(self, index):
        if (index < 0) or (index >= (self.__maxSize)):  #if out of range raise exception
            raise SparseArrayException("Index out of range")
        else:
            location = self.__head      #otherwise
            while location != None:
                if location.index == index:    #find node with index needed
                    return location.data       #return data contained in node
                location = location.next            
    
    def set(self, index, value):
        if (index < 0) or (index >= (self.__maxSize)):  #if out of range raise exception
            raise SparseArrayException("Index out of range")
        else:
            location = self.__head          #otherwise
            while location != None:
                if location.index == index:    #find node with index needed
                    location.data = value       #add the value as its data
                location = location.next            