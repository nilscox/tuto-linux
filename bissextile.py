def printYear(y, isLeap):
    y = str(y)
    if isLeap:
        print(y + " is a leap year")
    else:
        print(y + " is not a leap year")

def b(a):
    if a % 4 == 0 and a % 100 != 0:
        printYear(a, True)
    elif a % 400 == 0:
        printYear(a, True)
    else:
        printYear(a, False)

b(2009)
b(2092)
b(2042)
b(2012)
