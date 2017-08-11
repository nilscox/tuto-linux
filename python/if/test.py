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
    f = None
    try: f = isPositive
    except NameError: return

    a(f, [42], True)
    a(f, [123456789], True)
    a(f, [-1], False)
    a(f, [-123456789], False)
    a(f, [0], None)

def test_isOdd():
    f = None
    try: f = isOdd
    except NameError: return

    a(f, [2], False)
    a(f, [3], True)
    a(f, [0], False)
    a(f, [123456789], True)
    a(f, [876543210], False)
    a(f, [-1], True)
    a(f, [-2], False)

def test_isVowel():
    f = None
    try: f = isVowel
    except NameError: return

    a(f, ['a'], True)
    a(f, ['y'], True)
    a(f, ['b'], False)
    a(f, ['8'], False)

def test_max2():
    f = None
    try: f = max2
    except NameError: return

    a(f, [1, 2], 2)
    a(f, [2, 1], 2)
    a(f, [-1, 1], 1)

def test_max3():
    f = None
    try: f = max3
    except NameError: return

    a(f, [1, 2, 3], 3)
    a(f, [1, 3, 2], 3)
    a(f, [2, 1, 3], 3)
    a(f, [2, 3, 1], 3)
    a(f, [3, 1, 2], 3)
    a(f, [3, 2, 1], 3)

def test_daysInMonth():
    f = None
    try: f = daysInMonth
    except NameError: return
    a(f, [1], 31)
    a(f, [2], 28)
    a(f, [4], 30)
    a(f, [7], 31)
    a(f, [8], 31)
    a(f, [9], 30)
    a(f, [12], 31)

def test_areValidTriangleAngles():
    f = None
    try: f = areValidTriangleAngles
    except NameError: return
    a(f, [1, 2, 3], False)
    a(f, [60, 60, 60], True)
    a(f, [40, 50, 90], True)
    a(f, [1, 178, 1], True)
    a(f, [100, 30, 40], False)
    a(f, [-10, 10, 180], False)
    a(f, [-10, 30, 160], False)
    a(f, [0, 0, 0], False)
    a(f, [-1, -1, -1], False)

def test_areValidTriangleSides():
    f = None
    try: f = areValidTriangleSides
    except NameError: return
    a(f, [1, 2, 3], True)
    a(f, [5, 3, 4], True)
    a(f, [10, 1, 1], False)
    a(f, [1, 10, 1], False)
    a(f, [1, 1, 10], False)
    a(f, [10, 5, 5], True)
    a(f, [-1, 2, 3], False)
    a(f, [1, -2, 3], False)
    a(f, [1, 2, -3], False)

def test_areValidRightTriangleSides():
    f = None
    try: f = areValidRightTriangleSides
    except NameError: return
    a(f, [1, 2, 3], False)
    a(f, [5, 3, 4], True)
    a(f, [101, 99, 20], True)
    a(f, [-5, 3, 4], False)
    a(f, [5, -3, 4], False)
    a(f, [5, 3, -4], False)

def test_solveQuadratic():
    f = None
    try: f = solveQuadratic
    except NameError: return
    a(f, [1, 2, 3], None)
    a(f, [1, 3, 2], (-2., -1.))
    a(f, [2, 1, 3], None)
    a(f, [2, 3, 1], (-1., -0.5))
    a(f, [1, 2, 1], -1.)
    a(f, [1, 1, 0], (-1., 0.))
    a(f, [1, 0, 0], 0.)

def test_isSorted():
    f = None
    try: f = isSorted
    except NameError: return
    a(f, [[]], True)
    a(f, [[42]], True)
    a(f, [[42, 51]], True)
    a(f, [[51, 42]], True)
    a(f, [[1, 2, 3]], True)
    a(f, [[3, 2, 1]], True)
    a(f, [[-12, -8, 0, 1, 42, 123]], True)
    a(f, [[12, 8, -0, -1, -42, -123]], True)
    a(f, [[1, 3, 2]], False)
    a(f, [[3, 2, 3]], False)
    a(f, [[1, 2, 3, 5, 4, 6, 7]], False)

for f in [
    test_isPositive,
    test_isOdd,
    test_isVowel,
    test_max2,
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
