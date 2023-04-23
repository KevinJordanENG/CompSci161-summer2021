'''
Hey there! This is Lab 10a for CSCI 161 Summer 2021
Sorts alphabetically band names ignoring words of
'a', 'an', and 'the'. Uses bubble sort algorithm.
By Kevin Jordan kevin.jordan@und.edu 1301006
'''

def mySort(theList, ignoredWords):
    theList2 = []                   #new list for strings with chopped off start words
    for i in range(len(theList)):   #for the list
        if theList[i].lower().startswith(ignoredWords[0].lower()+' '):  #put in lower, does it have the 1st word to ignore?
            theList2.append(theList[i].lower().replace(ignoredWords[0].lower()+' ', '')) #append lower version with ignored word replaced with empty str
        elif theList[i].lower().startswith(ignoredWords[1].lower()+' '): #put in lower, does it have the 2nd word to ignore?
            theList2.append(theList[i].lower().replace(ignoredWords[1].lower()+' ', '')) #append lower version with ignored word replaced with empty str
        elif theList[i].lower().startswith(ignoredWords[2].lower()+' '): #put in lower, does it have the 3rd word to ignore?
            theList2.append(theList[i].lower().replace(ignoredWords[2].lower()+' ', '')) #append lower version with ignored word replaced with empty str       
        else:  # if it doesnt start with word to ignore
            theList2.append(theList[i].lower()) #add to copy list as is
    for j in range(len(theList2) -1): #for the number of items -1, pass over whole list
        swapped = False     #set flag for early break if no items get swapped and already sorted
        for i in range(len(theList2) -1):   #for each item
            if theList2[i] > theList2[i+1]: #if current item is bigger than next item theyre out of order    
                temp2 = theList2[i]             #swap item in copy chopped list to make sure bubble sort works
                theList2[i] = theList2[i+1]
                theList2[i+1] = temp2
                
                temp = theList[i]               #swap item in final list in same pattern as copy for final goal
                theList[i] = theList[i+1]
                theList[i+1] = temp
                swapped = True                  #change flag to know to keep looping outer for
        if swapped == False:                    #if none were swapped, list is already in order
            break                               #so break out

def main():
    theList = ['A Flock of Seagulls', 'Rush', 'The Cars', 'Trooper', 'J Balivn', 'Juanes', 'Bad Bunny', 'Centavrs']
    ignoredWords = ['A', 'An', 'The']
    print("OK, lets see what artists we have in this bin shall we?")
    print()
    for i in range(len(theList)):
        print(theList[i])
    print()
    print("Hmmmmm, these aren't even close to in order!")
    print("Lets get these in alphabetical order but,")
    print("lets ignore these starting words:", ignoredWords)
    print()
    mySort(theList, ignoredWords)
    for i in range(len(theList)):
        print(theList[i])
    print()
    print("Alright, much better!")
    print("Tata!")

main()