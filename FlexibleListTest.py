'''
Hey there! This is Lab 3b for CSCI 161 Summer 2021
Tests a class object that creates a fixed length list
and can have custom indexes set.
By Kevin Jordan kevin.jordan@und.edu 1301006
'''

from FlexibleList import *

x = FlexibleList(1990, 2000)
x.set(1995, 'XXX')
print(x.get(1995))
print(x.lowIndex())
print(x.highIndex())
print(x.isInList('XXX'))
print(x.indexOf('XX'))