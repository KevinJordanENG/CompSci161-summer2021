'''
Hey there! This is Lab 12a for CSCI 161 Summer 2021
Tests Binary Search Tree (BSTree) data structure.
Has new methods added such as isEmpty, min, max,
numOfLeaves, height, and complete. 
By Kevin Jordan kevin.jordan@und.edu 1301006 (and Tom Stokke, UND)
'''

from MyBSTree import *

def main ():
    t = MyBSTree()
    print ("Is it empty? ", t.isEmpty())
    print ("How many nodes? ", t.size())
    print("How many leaves? ", t.numOfLeaves())
    print("Lets insert 'm', 'b', 'e', 'd', 'a', 's', 't', 'o' in that order")
    t.insert ("m")
    t.insert ("b")
    t.insert ("e")
    t.insert ("d")
    t.insert ("a")
    t.insert ("s")
    t.insert ("t")
    t.insert ("o")
    print()
    print ("Is it empty? ", t.isEmpty())
    print ("How many nodes? ", t.size())    
    print("What is the minimun? ", t.min())
    print("What is the maximun? ", t.max())
    print("How many leaves? ", t.numOfLeaves())
    print("What is height of BSTree? ", t.height())
    print("Is the BSTree complete? ", t.complete())
    print()
    print()
    t2 = MyBSTree()
    print("Lets insert 'm', 'b', 'e', 'd', 'a', 's', 't', 'o', 'f' in that order")
    t2.insert ("m")
    t2.insert ("b")
    t2.insert ("e")
    t2.insert ("d")
    t2.insert ("a")
    t2.insert ("s")
    t2.insert ("t")
    t2.insert ("o")
    t2.insert ("f")
    print()
    print ("Is it empty? ", t2.isEmpty())
    print ("How many nodes? ", t2.size())    
    print("What is the minimun? ", t2.min())
    print("What is the maximun? ", t2.max())
    print("How many leaves? ", t2.numOfLeaves())
    print("What is height of BSTree? ", t2.height())
    print("Is the BSTree complete? ", t2.complete())
    print()
    print("SEEEEE Y'ALL LATERRRRR!!!!")

main() 