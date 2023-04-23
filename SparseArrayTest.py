'''
Hey there! This is Lab 11a2 for CSCI 161 Summer 2021
Tests a class object that uses linked lists to
generate a sparse array. Supports methods of get,
getDefaultValue, and set.
By Kevin Jordan kevin.jordan@und.edu 1301006
'''

from SparseArray import *

print("OKKKKY, so here we're trying out the SparseArray")
print("Creating object with defaultValue of '$'")
print("and maxSize of 5")
s = SparseArray('$', 5)
print()
print("Alright, it should have '$' as default, show me!")
print()
print(s.getDefaultValue())
print()
print("Oh, sorry yes this is correct but,")
print("I wanted to see the whole list, can I see that?")
print()
print("***Index numbers of nodes***")
print('0   1   2   3   4')
for i in range(5):
    print(s.get(i), end='   ')
print()
print()
print("Cool! So lets try and set index 3 as '%'")
s.set(3, '%')
print()
print("Can I see it to confirm it added?")
print()
print(s.get(3))
print()
print("Oh, sorry yes this is correct but,")
print("I wanted to see the whole list, can I see that?")
print()
print("***Index numbers of nodes***")
print('0   1   2   3   4')
for i in range(5):
    print(s.get(i), end='   ')
print()
print()
print("OOO Heuuuwl yeee! KKBYEE!")