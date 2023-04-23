'''
Hey there! This is Lab 7b for CSCI 161 Summer 2021
Tests a class object that behaves as a stack
datastructure. Similar to ListStack but updated
push method. This version of push removes last item
in stack and shifts all items down to accomodate new item.
By Kevin Jordan kevin.jordan@und.edu 1301006 (and Tom Stokke UND)
'''

from LimitedStack import *

print("Alright, lets test our new LimitedStack")
print("Setting max size to 3 for easy analysis")
s = LimitedStack(3)
print("Pushing 'a' onto top of stack")
s.push('a')
print("Whats at the top of the 1 item stack?")
print(s.peek())
print("Pushing 'b' onto top of stack")
s.push('b')
print("Whats at the top of the 2 item stack?")
print(s.peek())
print("Pushing 'c' onto top of stack")
s.push('c')
print("Whats at the top of the 3 item stack?")
print(s.peek())
print("Stack is now maxed at 3 items. If working,")
print("'d' should be pushed to top of stack")
s.push('d')
print("Stack full?", s.isFull())
print("OK, so the stack is still full of 3 items,")
print("and should have dropped the first item")
print("Lets pop off items to check if remaining are last 3 items")
print("Top item of 3 item stack")
print(s.pop())
print("Top item of 2 item stack")
print(s.pop())
print("Last item of stack. It should be a 'b'")
print(s.pop())
print("It was! Coolio bro, ciao for now!")