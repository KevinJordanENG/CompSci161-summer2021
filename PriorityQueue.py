'''
Hey there! This is Lab 8 for CSCI 161 Summer 2021
Creates a class object that acts as a queue with 
additional priority functionality allowing the addition
of items to the queue based on this priority reference.
By Kevin Jordan kevin.jordan@und.edu 1301006 (and Tom Stokke UND)
'''

class PriorityQueueError (Exception):
    pass

class PriorityQueue:
    
    class __Node:
        def __init__(self, item, priority):
            self.item = item                    #str item part of object
            self.priority = priority            #priority for proper queue placement

    def __init__ (self, maxSize=100):           #max size default to 100
        self.__queue = [None] * maxSize
        self.__maxSize = maxSize
        self.__numOfItems = 0

    def enqueue (self, itemToQueue, priority=1):    #priority defaults to 1 and added to function params
        if not self.isFull():                       
            itemToAdd2q = PriorityQueue.__Node(itemToQueue, priority)           #create node from inputs
            if itemToAdd2q.priority > 100 or (itemToAdd2q.priority < 1):        #if out of bounds raise exception
                raise PriorityQueueError ("Out of range of possible priority (1-100)")
            if self.__numOfItems == 0:                                  #if list is empty,
                index = 0                                               #index to add will be 0
            for i in range(0, self.__numOfItems):                       #in the list of nodes
                if self.__queue[i].priority < itemToAdd2q.priority:     #the first node priority less than one to add
                    index = i                                           #will be the index of item to be added
                    break                                               #break loop and keep index location
                else:                                                   #if nothing was less than
                    index = self.__numOfItems                           #end of list will be index to add newNode
            for j in range(0, self.__numOfItems - index):      #for the remaining nodes after the first less than
                self.__queue[self.__numOfItems - j] = self.__queue[self.__numOfItems -(1+j)]    #shift over from the back end
            self.__queue[index] = itemToAdd2q                           #wherever the above determined, add node
            self.__numOfItems += 1                                      #increment
        else:
            raise PriorityQueueError ("Unable to enqueue into a full queue")

    def front (self):
        if not self.isEmpty():
            return self.__queue[0]
        else:
            raise PriorityQueueError ("Unable to call firstItem from an empty queue")

    def removeFront(self)  :
        if not self.isEmpty():
            for index in range (0, self.__numOfItems - 1):
                self.__queue[index] = self.__queue[index + 1]
            self.__queue[self.__numOfItems - 1] = None #not required, as has been discussed more than once
            self.__numOfItems -= 1
        else:
            raise PriorityQueueError ("Unable to dequeue from an empty queue")

    def dequeue (self):
        if not self.isEmpty():
            itemToReturn = self.__queue[0]
            for index in range (0, self.__numOfItems - 1):
                self.__queue[index] = self.__queue[index + 1]
            self.__queue[self.__numOfItems - 1] = None #not required, as has been discussed more than once
            self.__numOfItems -= 1
            return itemToReturn.item            #########CHANGED TO RETURN ONLY str PART OF NODE OBJECT
        else:
            raise PriorityQueueError ("Unable to dequeue from an empty queue")

    def isEmpty (self):
        return self.__numOfItems == 0

    def isFull (self):
        return self.__numOfItems == self.__maxSize

    def maxSize(self):
        return self.__maxSize

    def __str__ (self):
        #if I was doing this "for real" I might do this:
        #return "ListQueue object - version 0.91, last updated 7/15/2021."
        strData = "Data: "
        for index in range (0, self.__numOfItems):
            strData += self.__queue[index] +  '  '
        return strData 