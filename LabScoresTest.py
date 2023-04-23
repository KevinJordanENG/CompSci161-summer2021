'''
Hey there! This is Lab 5 for CSCI 161 Summer 2021
Tests a class object that creates a fixed length list
to store Lab scores. This uses 1 based (human) indexing
and supports methods of get score, set score, number of scores,
total points, max value, min value, and average.
By Kevin Jordan kevin.jordan@und.edu 1301006
'''

from LabScores import *

s = LabScores(10)
print("So here is the original list created")
for i in range(1,11):
    print(s.getLabScore(i), end='  ')
print()
print("Lets see if set of 11 in index 6 was accepted")
print(s.setLabScore(6, 11))
print("Lets see if set of 20 in index 5 was accepted")
print(s.setLabScore(5, 20))
print("Lets see if set of -1 in index 2 was accepted")
print(s.setLabScore(2, -1))
print("Here is the new list with added items")
for i in range(1,11):
    print(s.getLabScore(i), end='  ')
print()
print("So whats the number of lab scores?")
print(s.getNumOfLabScores())
print("So whats the total number of points?")
print(s.getTotalPoints())
print("So whats the max non default value?")
print(s.getMaxValue())
print("So whats the min non default value?")
print(s.getMinValue())
print("So whats the average of scores?")
print(s.getAverage())
print("OK, thanks for testing class LabScores, toodel looo!")
