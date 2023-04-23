class ListQueueError (Exception):
   pass

class ListQueue:
   
   def __init__ (self, maxSize=10):
      #self.__queue = [None] * maxSize
      self.__queue = []
      for x in range (maxSize):
         self.__queue.append(None)
      self.__maxSize = maxSize
      self.__numOfItems = 0
      
   def enqueue (self, itemToQueue):
      if not self.isFull():
         self.__queue[self.__numOfItems] = itemToQueue
         self.__numOfItems += 1
      else:
         raise ListQueueError ("Unable to enqueue " + itemToQueue + " into a full queue")
   
   def front (self):
      if not self.isEmpty():
         return self.__queue[0]
      else:
         raise ListQueueError ("Unable to call firstItem from an empty queue")
   
   def removeFront(self)  :
      if not self.isEmpty():
         for index in range (0, self.__numOfItems - 1):
            self.__queue[index] = self.__queue[index + 1]
         self.__queue[self.__numOfItems - 1] = None #not required, as has been discussed more than once
         self.__numOfItems -= 1
      else:
         raise ListQueueError ("Unable to dequeue from an empty queue")
      
   def dequeue (self):
      if not self.isEmpty():
         itemToReturn = self.__queue[0]
         for index in range (0, self.__numOfItems - 1):
            self.__queue[index] = self.__queue[index + 1]
         self.__queue[self.__numOfItems - 1] = None #not required, as has been discussed more than once
         self.__numOfItems -= 1
         return itemToReturn
      else:
         raise ListQueueError ("Unable to dequeue from an empty queue")
   
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
   