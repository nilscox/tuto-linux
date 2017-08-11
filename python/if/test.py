from exos import *

def a(f, args, expected):
    actual = f(*args)
    if actual != expected:
        print('[\033[31mKO\033[0m] ' + f.__name__ + '(' + ', '.join(map(str, args)) + ')')
        print('expected: ' + str(expected))
        print('actual: ' + str(actual))
    else:
        print('[\033[32mOK\033[0m] ' + f.__name__ + '(' + ', '.join(map(str, args)) + ')')

def test_isPositive():
    try: isPositive
    except NameError: return
    a(isPositive, [42], True)
    a(isPositive, [123456789], True)
    a(isPositive, [-1], False)
    a(isPositive, [-123456789], False)
    a(isPositive, [0], None)

def test_isOdd():
    try: isOdd
    except NameError: return
    a(isOdd, [2], False)
    a(isOdd, [3], True)
    a(isOdd, [0], False)
    a(isOdd, [123456789], True)
    a(isOdd, [876543210], False)
    a(isOdd, [-1], True)
    a(isOdd, [-2], False)

def test_isVowel():
    try: isVowel
    except NameError: return
    a(isVowel, ['a'], True)
    a(isVowel, ['y'], True)
    a(isVowel, ['b'], False)
    a(isVowel, ['8'], False)

def test_max():
    try: max
    except NameError: return
    a(max, [1, 2], 2)
    a(max, [2, 1], 2)

def test_max3():
    try: max3
    except NameError: return
    a(max3, [1, 2, 3], 3)
    a(max3, [1, 3, 2], 3)
    a(max3, [2, 1, 3], 3)
    a(max3, [2, 3, 1], 3)
    a(max3, [3, 1, 2], 3)
    a(max3, [3, 2, 1], 3)

def test_daysInMonth():
    try: daysInMonth
    except NameError: return
    a(daysInMonth, [1], 31)
    a(daysInMonth, [2], 28)
    a(daysInMonth, [4], 30)
    a(daysInMonth, [7], 31)
    a(daysInMonth, [8], 31)
    a(daysInMonth, [9], 30)
    a(daysInMonth, [12], 31)

def test_areValidTriangleAngles():
    try: areValidTriangleAngles
    except NameError: return
    a(areValidTriangleAngles, [1, 2, 3], False)
    a(areValidTriangleAngles, [60, 60, 60], True)
    a(areValidTriangleAngles, [40, 50, 90], True)
    a(areValidTriangleAngles, [1, 178, 1], True)
    a(areValidTriangleAngles, [100, 30, 40], False)
    a(areValidTriangleAngles, [-10, 10, 180], False)
    a(areValidTriangleAngles, [-10, 30, 160], False)
    a(areValidTriangleAngles, [0, 0, 0], False)
    a(areValidTriangleAngles, [-1, -1, -1], False)

def test_areValidTriangleSides():
    try: areValidTriangleSides
    except NameError: return
    a(areValidTriangleSides, [1, 2, 3], False)
    a(areValidTriangleSides, [5, 3, 4], True)
    a(areValidTriangleSides, [101, 99, 20], True)

def test_solveQuadratic():
    try: solveQuadratic
    except NameError: return
    a(solveQuadratic, [1, 2, 3], None)
    a(solveQuadratic, [1, 3, 2], (-2., -1.))
    a(solveQuadratic, [2, 1, 3], None)
    a(solveQuadratic, [2, 3, 1], (-1., -0.5))
    a(solveQuadratic, [1, 2, 1], -1.)
    a(solveQuadratic, [1, 1, 0], (-1., 0.))
    a(solveQuadratic, [1, 0, 0], 0.)

def test_isSorted():
    try: isSorted
    except NameError: return
    a(isSorted, [[]], True)
    a(isSorted, [[42]], True)
    a(isSorted, [[42, 51]], True)
    a(isSorted, [[51, 42]], True)
    a(isSorted, [[1, 2, 3]], True)
    a(isSorted, [[3, 2, 1]], True)
    a(isSorted, [[-12, -8, 0, 1, 42, 123]], True)
    a(isSorted, [[12, 8, -0, -1, -42, -123]], True)
    a(isSorted, [[1, 3, 2]], False)
    a(isSorted, [[3, 2, 3]], False)
    a(isSorted, [[1, 2, 3, 5, 4, 6, 7]], False)

for f in [
    test_isPositive,
    test_isOdd,
    test_isVowel,
    test_max,
    test_max3,
    test_daysInMonth,
    test_daysInMonth,
    test_areValidTriangleAngles,
    test_areValidTriangleSides,
    test_solveQuadratic,
    test_isSorted,
]:
    print(f.__name__)
    print(len(f.__name__) * '-')
    f()
    print()
