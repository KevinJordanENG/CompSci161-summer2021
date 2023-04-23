'''
Hey there! This is Lab 5 for CSCI 161 Summer 2021
Creates a class object that creates a fixed length list
to store Lab scores. This uses 1 based (human) indexing
and supports methods of get score, set score, number of scores,
total points, max value, min value, and average.
By Kevin Jordan kevin.jordan@und.edu 1301006
'''

class IllegalLabError (Exception):      #nifty special exception
    pass                                #no need to do anything

class LabScores:                        #class created w/ class variable
    NO_VALUE = -1
    
    def __init__(self, maxSize):        #contructor
        
        self.__data = [self.NO_VALUE] * maxSize     #list created
        self.__highIndex = maxSize                  #max is also high index
        
    def getLabScore(self, index):
        if (index < 1) or (index > self.__highIndex):
            raise IllegalLabError("Out of range of accessible scores in LabScores")
        else:
            return self.__data[index-1]
        
    def setLabScore(self, index, score):
        if (index < 1) or (index > self.__highIndex):
            raise IllegalLabError("Out of range of accessible scores in LabScores")        
        else:
            if (score < 0) or (score > 150):
                return False
            else:
                self.__data[index-1] = score
                return True
    
    def getNumOfLabScores(self):
        count = 0
        for i in range(self.__highIndex-1):
            if self.__data[i] != self.NO_VALUE:
                count += 1
        return count
    
    def getTotalPoints(self):
        total = 0
        for i in range(self.__highIndex-1):
            if self.__data[i] != self.NO_VALUE:
                total += self.__data[i]
        return total        
    
    def getMaxValue(self):
        maxVal = -1
        for i in range(self.__highIndex-1):
            if self.__data[i] > maxVal:
                maxVal = self.__data[i]
        if maxVal == -1:
            return self.NO_VALUE
        else:
            return maxVal
    
    def getMinValue(self):
        minVal = 151
        for i in range(self.__highIndex-1):
            if (self.__data[i] < minVal) and (self.__data[i] != -1):
                minVal = self.__data[i]
        if minVal == 151:
            return self.NO_VALUE
        else:
            return minVal  
    
    def getAverage(self):
        scores = self.getNumOfLabScores()
        points = self.getTotalPoints()
        if scores == 0:
            return self.NO_VALUE
        return points/scores