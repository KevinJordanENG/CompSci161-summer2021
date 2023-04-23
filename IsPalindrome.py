'''
Hey there! This is Lab 7a for CSCI 161 Summer 2021
Uses pre-designed stack and queue class objects to
creat a program that determines if an input string
is or is not a palindrome. Adds individual characters
to both stack and queue, as removed difference confirms
not a palindrome. Otherwise, confirmed a palindrome.
By Kevin Jordan kevin.jordan@und.edu 1301006
'''

from ListStack import *
from ListQueue import *

def main():                                                     #main program
    print("Enter text to check if it is a palindrome")          #call for input
    initialString = input()                                     #input
    while initialString != '':                                  #while not exit condititon
        while (len(initialString) > 100):                       #while over char limit
            print("Sorry, 100 characters maximum")              #ask for new input within bounds
            print("Enter text to check if it is a palindrome")  #call for input
            initialString = input()                             #input
        stringChars = list(initialString.lower())               #make all lower and split str into list of chars
        stk = ListStack(len(initialString))                     #create stack object with len of input str
        q = ListQueue(len(initialString))                       #create queue object with len of input str
        for i in range(len(stringChars)):                       #for each char
            stk.push(stringChars[i])                            #add it to stack 
            q.enqueue(stringChars[i])                           #add it to queue
        f = None                                                #set flag
        for i in range(len(stringChars)):                       #for each char
            if stk.pop() != q.dequeue():                        #if return from stack and queue dont match
                f = False                                       #change flag
        if f == False:                                          #if flag is changed
            print(initialString, "is not a palindrome")         #tell user not palindrome
        else:
            print(initialString, "is a pallindrome!")           #if flag not changed, it's a palindrome
        print("Enter text to check if it is a palindrome")      #call for next input
        initialString = input()                                 #input

main()                                                          #LETS GOOOOOO!!!!