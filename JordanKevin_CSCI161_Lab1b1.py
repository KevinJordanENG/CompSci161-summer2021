'''
Hey there! This is Lab 1b1 for CSCI 161 Summer 2021
Writes entered test score info to file
By Kevin Jordan kevin.jordan@und.edu 1301006
'''

def main():
    import FileUtils
    fileName = FileUtils.selectSaveFile("Save File")
    if fileName == None:
        print("Chu didn't select anything bud!")
        exit()
    print("Enter scores. -1 to end and Save")
    outFile = open(fileName, "w")
    score = input()
    while score != '-1':
        outFile.write(score + '\n')
        score = input()
    outFile.close()

main()