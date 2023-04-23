'''
Hey there! This is Lab 4 for CSCI 161 Summer 2021
Tests a class object that creates a fixed length list.
Includes numerous methods such as add, remove, isInList,
isFull, isEmpty, getNextItem, size, reset, findIndexOf,
removeAll, replaceAll, count, partialMatch
By Kevin Jordan kevin.jordan@und.edu 1301006 (and Tom Stokke UND)
'''

from UnsortedList2 import *

ul = UnsortedList2()
ul.add('aaa')
ul.add('ll')
ul.add('aft')
ul.add('abe')
ul.add('and')
ul.add('at')
ul.add('all')
ul.add('all')
print(ul.count('all'))          #Test of count function
print()
for x in range (ul.size()):     #print of list items (original)
    print (ul.getNextItem())
print()
print(ul.replaceAll('XXX', 'at'))    #prints number replaced
print()
for x in range (ul.size()):          #prints list after replacement for validation
    print (ul.getNextItem())
print()
print(ul.removeAll('XXX'))          #prints number removed
print()
for x in range (ul.size()):         #prints new list after removal for validation
    print (ul.getNextItem())
print()
print(ul.partialMatch('ll'))        #prints all occurrences of searched charachters
