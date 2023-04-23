'''
Hey there! This is Lab 3a Part2 for CSCI 161 Summer 2021
Tests a class object that stores first/last name
and age. Contains comparison methods for name, age,
and equals for all object values
By Kevin Jordan kevin.jordan@und.edu 1301006
'''

from Friend import *

kevin1 = Friend()
kevin2 = Friend("Kevin", "Jordan", 27)
kevin1.setFirstName("Kevin")
kevin1.setLastName("Jordan")
kevin1.setAge(27)
print("First name:      ", kevin1.getFirstName())
print("Last name:       ", kevin1.getLastName())
print("Age:             ", kevin1.getAge())
print("Same age?        ", kevin1.isSameAge(kevin2))
print("Same name?       ", kevin1.isSameName(kevin2))
print("Exact same?      ", kevin1.equals(kevin2))