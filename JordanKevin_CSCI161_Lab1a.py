'''
Hey there! This is Lab 1a for CSCI 161 Summer 2021
Program converts temperature from C, F, K to any other
By Kevin Jordan kevin.jordan@und.edu 1301006
'''

def getMenuChoice():
    print()
    print("Choose conversion:")
    print("1. Fahrenheit to Celsius")
    print("2. Fahrenheit to Kelvin")
    print("3. Celsius to Fahrenheit")
    print("4. Celsius to Kelvin")
    print("5. Kelvin to Fahrenheit")
    print("6. Kelvin to Celsius")
    print("7. Quit")
    print()
    choice = int(input("Selection: "))
    while (choice > 7) or (choice < 1):
        print("Enter a valid selection 1-7")
        choice = int(input())
    return choice

def FtoC(F):
    C = (F-32) * (5/9)
    return C

def FtoK(F):
    K = FtoC(F) + 273.15
    return K

def CtoF(C):
    F = (C*(9/5)) + 32
    return F

def CtoK(C):
    K = C + 273.15
    return K

def KtoC(K):
    C = K - 273.15
    return C

def KtoF(K):
    F = (KtoC(K))*(9/5) + 32
    return F

def main():
    print("Welome to the temperature converter")
    choice = getMenuChoice()
    while choice != 7:
        if choice == 1:
            temp = float(input("Temp to convert: "))
            print(temp, " degF is: ", format(FtoC(temp), "8.2f"), " degC", sep='')
        elif choice == 2:
            temp = float(input("Temp to convert: "))
            print(temp, " degF is: ", format(FtoK(temp), "8.2f"), " K", sep='')
        elif choice == 3:
            temp = float(input("Temp to convert: "))
            print(temp, " degC is: ", format(CtoF(temp), "8.2f"), " degF", sep='')
        elif choice == 4:
            temp = float(input("Temp to convert: "))
            print(temp, " degC is: ", format(CtoK(temp), "8.2f"), " K", sep='') 
        elif choice == 5:
            temp = float(input("Temp to convert: "))
            print(temp, " K is: ", format(KtoF(temp), "8.2f"), " degF", sep='') 
        elif choice == 6:
            temp = float(input("Temp to convert: "))
            print(temp, " K is: ", format(KtoC(temp), "8.2f"), " degC", sep='') 
        choice = getMenuChoice()

main()