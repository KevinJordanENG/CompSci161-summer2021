from ListQueue import ListQueue, ListQueueError
#from ListQueue2 import ListQueue2, ListQueue2Error

def main():
   queue = ListQueue2 (5)
   queue.enqueue ("a")
   print ("Current queue ", queue)
   queue.enqueue ("b")
   print ("Current queue ", queue)
   queue.enqueue ("c")
   print ("Current queue ", queue)
   queue.enqueue ("d")
   print ("Current queue ", queue)
   queue.enqueue ("e")
   print ("Current queue ", queue)
   if not queue.isFull():
      queue.enqueue ("f")
      print ("Current queue ", queue)
   else:
      print ("Can't add f, queue is full")
   
   while queue.isEmpty() != True:
      firstItem = queue.dequeue()
      print ("Item removed from queue ", firstItem)
      print ("Current queue ", queue)
      print ()

   for x in range (100000):
      queue.enqueue ("x")
      value = queue.dequeue()
      #print (x)
   print ("done")

main()   