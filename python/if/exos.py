from math import sqrt

def isPositive(a):
    if a == 0:
        return None
    return a > 0

def isOdd(a):
    return a % 2 is not 0

def isVowel(c):
    return ['a', 'e', 'i', 'o', 'u', 'y'].count(c) != 0

def max2(a, b):
    return a if a > b else b

def max3(a, b, c):
    return max2(max2(a, b), c)

def med(a, b, c):
    if a > b:
        if b > c:
            return b
        elif a > c:
            return c
        else:
            return a
    else:
        if a > c:
            return a
        elif b > c:
            return c
        else:
            return b

def daysInMonth(n):
    if n == 2:
        return 28
    if n <= 7:
        if n % 2:
            return 31
        else:
            return 30
    else:
        if n % 2:
            return 30
        else:
            return 31

def areValidTriangleAngles(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b + c == 180

def areValidTriangleSides(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False

    def calculate(a, b, c):
        return a + b >= c

    h = max3(a, b, c)

    if h == a:
        return calculate(b, c, a)
    elif h == b:
        return calculate(a, c, b)
    else:
        return calculate(a, b, c)

def areValidRightTriangleSides(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False

    def calculate(a, b, c):
        return a * a + b * b == c * c

    h = max3(a, b, c)

    if h == a:
        return calculate(b, c, a)
    elif h == b:
        return calculate(a, c, b)
    else:
        return calculate(a, b, c)

def solveQuadratic(a, b, c):
    delta = b * b - 4 * a * c
    if delta < 0:
        return None
    elif delta == 0:
        return -b / (2 * a)
    else:
        return ((-b - sqrt(delta)) / (2 * a), (-b + sqrt(delta)) / (2 * a))

def isSorted(l):
    if len(l) <= 2:
        return True

    a = l[0]
    b = l[1]

    if l[0] < l[1]:
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                return False
    else:
        for i in range(len(l) - 1):
            if l[i] < l[i + 1]:
                return False
    return True
