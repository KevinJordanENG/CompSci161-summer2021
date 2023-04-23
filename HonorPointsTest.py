'''
Hey there! This is Lab 2 for CSCI 161 Summer 2021
Tests a class object to track honor points and
credits to help calc GPA for seperate students.
Can also show how close to graduation.
By Kevin Jordan kevin.jordan@und.edu 1301006
'''

from HonorPoints import HonorPoints

mike = HonorPoints("Mike Row")
mike.addClass(4, "b")
mike.addClass(3, "c")
mike.addClass(2, "f")
mike.addClass(4, "A")
kevin = HonorPoints()
kevin.setName("Kevin Jordan")
kevin.addClass(4, "b")
kevin.addClass(4, "A")
print("Name                    ", kevin.getName())
print("Total credits           ", kevin.getCredits())
print("Total passed credits    ", kevin.getPassedCredits())
print("Honor points            ", kevin.getHonorPoints())
print("GPA                     ", kevin.getGPA())
print("Are they smarter?       ", kevin.isSmarter(mike))
print("Can they graduate?      ", kevin.canGraduate())