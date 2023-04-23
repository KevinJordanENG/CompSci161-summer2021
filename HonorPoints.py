'''
Hey there! This is Lab 2 for CSCI 161 Summer 2021
Creates a class object to track honor points and
credits to help calc GPA for seperate students.
Can also show how close to graduation.
By Kevin Jordan kevin.jordan@und.edu 1301006
'''

class HonorPoints:
    REQUIRED_CREDITS = 20   #set class variables
    NO_GPA = -1
    
    def __init__(self, name = ''):  
        self.__name = name          #set private instance variables
        self.__totalCredits = 0
        self.__honorPoints = 0
        self.__totalPassedCredits = 0
        
    def addClass(self, numCredits, letterGrade):
        if (numCredits < 1) or (numCredits > 8):        #error checking for erronious credit numbers
            return False
        else:
            self.__totalCredits = self.__totalCredits + numCredits          #add to running total
        if (letterGrade == "A") or (letterGrade == "a"):                    #check for usable leter grades
            hPoints = 4*numCredits                                          #calc honor points
            self.__honorPoints = self.__honorPoints + hPoints
            self.__totalPassedCredits = self.__totalPassedCredits + numCredits
        elif (letterGrade == "B") or (letterGrade == "b"):
            hPoints = 3*numCredits
            self.__honorPoints = self.__honorPoints + hPoints
            self.__totalPassedCredits = self.__totalPassedCredits + numCredits
        elif (letterGrade == "C") or (letterGrade == "c"):
            hPoints = 2*numCredits
            self.__honorPoints = self.__honorPoints + hPoints
            self.__totalPassedCredits = self.__totalPassedCredits + numCredits
        elif (letterGrade == "D") or (letterGrade == "d"):
            hPoints = 1*numCredits
            self.__honorPoints = self.__honorPoints + hPoints
            self.__totalPassedCredits = self.__totalPassedCredits + numCredits
        elif (letterGrade == "F") or (letterGrade == "f"):
            self.__honorPoints = self.__honorPoints + 0
            self.__totalPassedCredits = self.__totalPassedCredits + 0
        else:
            return False
        return True
        
    def setName(self, name):
        self.__name = name
        return True
    
    def getName(self):
        return self.__name
    
    def getCredits(self):
        return self.__totalCredits
    
    def getPassedCredits(self):
        return self.__totalPassedCredits
    
    def getHonorPoints(self):
        return self.__honorPoints
    
    def getGPA(self):
        if self.__totalCredits == 0:
            return self.NO_GPA
        else:
            GPA = self.__honorPoints / self.__totalCredits
            return GPA
        
    def isSmarter(self, otherStudent):
        if type(self) != type(otherStudent):
            print("ERROR: INCONSISTENT TYPE")               #error msg
            exit()
        if self.getGPA() > otherStudent.getGPA():
            return True
        else:
            return False
    
    def canGraduate(self):
        if self.__totalPassedCredits >= self.REQUIRED_CREDITS:
            return True
        else:
            return False
        
        