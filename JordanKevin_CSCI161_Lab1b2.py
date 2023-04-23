'''
Hey there! This is Lab 1b2 for CSCI 161 Summer 2021
Reads numbers from file and displays mean, median, mode
By Kevin Jordan kevin.jordan@und.edu 1301006
'''
def calcMedian(scoresList):
    scoresList.sort()
    if len(scoresList) % 2 == 1:
        i = int((len(scoresList)-1)/2)
        median = scoresList[i]
    else:
        i1 = int((len(scoresList)/2) - 1)
        i2 = i1+1
        median = (scoresList[i1]+scoresList[i2])/2
    return median

def findMode(scoresList):
    Max = max(scoresList)
    t = Max + 1
    count = [0] * t
    for i in range(t):
        count[i]=0
    for i in range(len(scoresList)):
        count[scoresList[i]] += 1
    mode = 0
    k = count[0]
    for i in range(1, t):
        if (count[i]>k):
            k = count[i]
            mode = i
    return mode
    
def main():
    import FileUtils
    fileName = FileUtils.selectOpenFile("Open File")
    if fileName == None:
        print("Nothin selected amigo, try again!")
        exit()    
    readFile = open(fileName, "r")
    scoresList = []
    for line in readFile:
        scoresList.append(int(line.strip()))
    readFile.close()
    if scoresList == []:
        print("Sorry brohan, no data in that file")
    else:
        print("Mean:", format(sum(scoresList)/len(scoresList), "10.3f"))
        print("Median:", format(calcMedian(scoresList), "6.1f"))
        print("Mode:", format(findMode(scoresList), "6"))
          
main()