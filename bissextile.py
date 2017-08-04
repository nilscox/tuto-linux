def printYear(y):
    leap = isLeap(int(y))
    if leap:
        print(y + " is a leap year")
    else:
        print(y + " is not a leap year")

def isLeap(y):
    return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0

printYear(input("enter a year number: "))
