'''
Hey there! This is Lab 3a Part1 for CSCI 161 Summer 2021
Creates a class object that stores first/last name
and age. Contains comparison methods for name, age,
and equals for all object values
By Kevin Jordan kevin.jordan@und.edu 1301006
'''

class Friend:
    
    def __init__(self, firstName = '', lastName = '', age = -1):
        
        self.__firstName = firstName
        self.__lastName = lastName
        self.__age = age
        
    def setFirstName(self, first):
        self.__firstName = first
        return True
    
    def setLastName(self, last):
        self.__lastName = last
        return True
    
    def setAge(self, age):
        if (age < 0) or (age > 130):
            return False
        else:
            self.__age = age
            return True
        
    def getFirstName(self):
        return self.__firstName
    
    def getLastName(self):
        return self.__lastName
    
    def getAge(self):
        return self.__age
    
    def isSameAge(self, friend):
        if type(self) != type(friend):
            print("ERROR: INCONSISTENT TYPE")               #error msg
            exit()
        else:
            if self.__age == friend.__age:
                return True
            else:
                return False
    
    def isSameName(self, friend):
        if type(self) != type(friend):
            print("ERROR: INCONSISTENT TYPE")               #error msg
            exit()
        else:
            if (self.__firstName.lower() == friend.__firstName.lower()) \
            and (self.__lastName.lower() == friend.__lastName.lower()):
                return True
            else:
                return False
            
    def equals(self, friend):
        if type(self) != type(friend):
            print("ERROR: INCONSISTENT TYPE")               #error msg
            exit()
        else:
            if (self.__firstName == friend.__firstName) \
            and (self.__lastName == friend.__lastName) \
            and (self.__age == friend.__age):
                return True
            else:
                return False
            